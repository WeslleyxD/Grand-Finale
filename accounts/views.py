from rest_framework import viewsets

from .serializers import UserSerializer, ChangePasswordSerializer, UserTypeSerializer
from .permissions import IsOwnerOrReadOnly
from accounts.models import User, UserType
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action, permission_classes
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    @action(detail=True, methods=['POST'], permission_classes=([IsAdminUser]))
    def set_password(self, request, pk=None):

        user = self.get_object()
        change_password_serializer = ChangePasswordSerializer(data=request.data)

        if change_password_serializer.is_valid():
            data = change_password_serializer.validated_data

            user.set_password(data['new_password'])
            user.save()

            return Response({'detail': _("Password updated successfully.")}, status=status.HTTP_200_OK)

        return Response({'errors': change_password_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        # Remove the "password" field from the validated data dictionary
        if 'password' in request.data:
            return Response({'errors': _('Update')}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)


class UserTypeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
    permission_classes = [IsAuthenticated]