from django.contrib import admin
from home.models import Stock,Setting
from .forms import StockCreateForm

# Register your models here.

class StockCreateForm(admin.ModelAdmin):
	list_display = ['category', 'item_name', 'quantity', 'price']
	form = StockCreateForm
	list_filter = ['category', 'item_name']
	search_fields = ['category', 'item_name']


admin.site.register(Stock, StockCreateForm)
admin.site.register(Setting)