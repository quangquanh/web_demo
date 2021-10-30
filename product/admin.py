from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Product_type) # đămg ký class loại sản phẩm trong admin
admin.site.register(models.Product)# đămg ký class sản phẩm trong admin
admin.site.register(models.Picture)# đămg ký class ảnh sản phẩm trong admin
admin.site.register(models.Order)# đămg ký class đặt hàng trong admin