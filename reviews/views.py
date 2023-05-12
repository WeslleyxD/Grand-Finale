from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewSerializer

# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]