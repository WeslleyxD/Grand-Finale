from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Coupon
from .serializers import CouponSerializer

# Create your views here.

class CouponViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated]