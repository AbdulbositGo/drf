from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet


router = DefaultRouter()
router.register('products', ProductViewSet, basename="products")
print(dir(router.urls[0]))
for i in router.urls:
    print(i.name)
    print(i.resolve)
    print(i.pattern)
urlpatterns = router.urls
