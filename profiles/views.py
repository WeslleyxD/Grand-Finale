from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Owner, ClientUser
from .serializers import OwnerSerializer, ClientUserSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticated]

class ClientUserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserSerializer
    permission_classes = [IsAuthenticated]