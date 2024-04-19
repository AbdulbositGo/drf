from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet


router = DefaultRouter()
router.register('products', ProductViewSet, basename="products")
print(dir(router.urls[0]))
urlpatterns = router.urls
