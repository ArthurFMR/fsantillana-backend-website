from rest_framework import viewsets
from rest_framework import mixins
from .models import CompanyInfo, Slides, Services, Products
from .serializer import CompanyInfoSerial, SlidesSerial, ServicesSerial, ProductsSerial


class CompanyInfoViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin ,viewsets.GenericViewSet):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerial


class SlidesViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin ,viewsets.GenericViewSet):
    queryset = Slides.objects.all()
    serializer_class = SlidesSerial
    

class ServicesViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin ,viewsets.GenericViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerial


class ProductsViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin ,viewsets.GenericViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerial