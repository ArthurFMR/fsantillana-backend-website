from django.contrib import admin
from .models import CompanyInfo, Slides, Services, Products

# Register your models here.
admin.site.register(CompanyInfo)
admin.site.register(Slides)
admin.site.register(Services)
admin.site.register(Products)