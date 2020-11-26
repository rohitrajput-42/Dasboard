from django.contrib import admin
from .models.data import Data
from .models.category import Category

class AdminData(admin.ModelAdmin):
    list_display = ['awbno', 'startdate', 'etd', 'status', 'category'] 

admin.site.register(Data, AdminData)
admin.site.register(Category)