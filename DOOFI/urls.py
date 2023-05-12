from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from accounts.views import UserViewSet, UserTypeViewSet
from coupons.views import CouponViewSet
from orders.views import OrderViewSet, OrderItemViewSet
from payments.views import PaymentViewSet
from products.views import ProductViewSet, CategoryViewSet
from profiles.views import OwnerViewSet, ClientUserViewSet
from reviews.views import ReviewViewSet
from stores.views import StoreViewSet, StoreAddressViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'user-type', UserTypeViewSet, basename="user-type")
router.register(r'coupons', CouponViewSet, basename="coupons")
router.register(r'orders', OrderViewSet,basename="order")
router.register(r'order-items', OrderItemViewSet,basename="order-items")
router.register(r'payments', PaymentViewSet,basename="payments")
router.register(r'products', ProductViewSet,basename="products")
router.register(r'categories', CategoryViewSet,basename="categories")
router.register(r'owners', OwnerViewSet, basename="owners")
router.register(r'client-user', ClientUserViewSet, basename="client-user")
router.register(r'reviews', ReviewViewSet, basename="reviews")
router.register(r'stores', StoreViewSet, basename="stores")
router.register(r'store-address', StoreAddressViewSet, basename="store-address")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)