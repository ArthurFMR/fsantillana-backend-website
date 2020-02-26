from django.contrib import admin
from .models import CompanyInfo, Slides, Services, Products

# Register your models here.

class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price', 'category',)
    search_fields = ('name',)



admin.site.register(CompanyInfo)
admin.site.register(Slides, SlideAdmin)
admin.site.register(Services, ServiceAdmin)
admin.site.register(Products, ProductAdmin)