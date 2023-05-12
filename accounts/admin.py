from django.contrib import admin

# Register your models here.

from .models import User, UserType

class UserAdmin(admin.ModelAdmin):
    # readonly_fields = ('email',)
    pass

admin.site.register(User, UserAdmin)
admin.site.register(UserType)