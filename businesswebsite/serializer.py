from rest_framework import serializers
from .models import CompanyInfo, Slides, Services, Products

class CompanyInfoSerial(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'

class SlidesSerial(serializers.ModelSerializer):
    class Meta:
        model = Slides
        fields = '__all__'

class ServicesSerial(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class ProductsSerial(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'