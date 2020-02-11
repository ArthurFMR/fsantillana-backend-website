from rest_framework import routers

from .viewsets import CompanyInfoViewSet, SlidesViewSet, ServicesViewSet, ProductsViewSet

router = routers.SimpleRouter()
router.register('companyinfo', CompanyInfoViewSet)
router.register('slides', SlidesViewSet)
router.register('services', ServicesViewSet)
router.register('products', ProductsViewSet)   

urlpatterns = router.urls