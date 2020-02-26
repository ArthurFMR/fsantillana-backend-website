from django.db import models
from model_utils import Choices

# Create your models here.


class CompanyInfo(models.Model):
    company_name = models.TextField()
    subtitle_name = models.TextField()
    tel = models.TextField()
    whatsapp = models.TextField(null=True, blank=True)
    address = models.TextField()
    email = models.TextField()
    facebook = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    about = models.TextField()
    short_about = models.CharField(max_length=140)
    building_img = models.ImageField(
        null=True, blank=True, upload_to='images/')
    logo = models.ImageField(
        upload_to='images/', default='image/logo-default.jpg')
    src_googlemap = models.TextField(null=True, blank=True)
    schedule_monday_friday = models.CharField(max_length=100)
    schedule_saturday = models.CharField(max_length=100)
    schedule_sunday = models.CharField(max_length=100)
    schedule_holidays = models.CharField(max_length=100, null=True, blank=True)


class Slides(models.Model):
    slide_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    description = models.TextField()
    img = models.ImageField(upload_to='images/slides/',
                            default='images/default-slide.jpg')

    def __str__(self):
        return 'Slide: ' + self.title


class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    img = models.ImageField(upload_to='images/services/',
                            default='images/default.png')

    def __str__(self):
        return 'Service: ' + self.title


class Products(models.Model):
    CATEGORY = Choices('', 'office', 'school', 'cel_accessory', 'desktop', 'Laptop', 'pc_accessory',
                       'pc_components')

    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    old_price = models.FloatField(null=True, blank=True)
    category = models.TextField(choices=CATEGORY, default='')
    img = models.ImageField(upload_to='images/products/',
                            default='images/default.png')

    def __str__(self):
        return 'Product: ' + self.name
