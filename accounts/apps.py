# from django.apps import AppConfig


# class AccountsConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'accounts'


import sys
from urllib.parse import urlparse

from django.apps import AppConfig
from django.conf import settings


class CommonConfig(AppConfig):
    name = "accounts"
    verbose_name = "Common"

    def ready(self):
        if settings.DEV_SERVER and settings.USE_NGROK:
            # pyngrok will only be installed, and should only ever be initialized, in a dev environment
            from pyngrok import ngrok

            # Get the dev server port (defaults to 8000 for Django, can be overridden with the
            # last arg when calling `runserver`)
            addrport = urlparse("http://{}".format(sys.argv[-1]))
            port = addrport.port if addrport.netloc and addrport.port else 8000

            # Open a ngrok tunnel to the dev server
            public_url = ngrok.connect(port).public_url
            url = "ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port)
            print(url)

            # Update any base URLs or webhooks to use the public ngrok URL
            settings.BASE_URL = public_url
            CommonConfig.init_webhooks(public_url)

    @staticmethod
    def init_webhooks(base_url):
        # Update inbound traffic via APIs to use the public-facing ngrok URL
        pass