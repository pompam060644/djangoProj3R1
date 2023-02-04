from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Goods)
admin.site.register(GoodsCategory)
admin.site.register(Order)
admin.site.register(OderDetails)
