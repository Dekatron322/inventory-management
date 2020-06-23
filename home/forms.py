from django import forms
from .models import Stock
from django.contrib import messages
class StockCreateForm(forms.ModelForm):
	class Meta:
		model = Stock

		fields = ['category', 'item_name', 'barcode', 'reorder_level', 'quantity', 'price', 'sold_quantity',]

	def clean_category(self):
		category = self.cleaned_data.get('category')
		if not category:
			raise forms.ValidationError('This field is required')

		for instance in Stock.objects.all():
			if instance.category == category:
				raise forms.ValidationError(category + ' already exists')
		return category

	def clean_barcode(self):
		barcode = self.cleaned_data.get('barcode')
		if not barcode:
			raise forms.ValidationError('This field is required')

		for instance in Stock.objects.all():
			if instance.barcode == barcode:
				raise forms.ValidationError(barcode + ' already exists')
		return barcode



	def clean_item_name(self):
		item_name = self.cleaned_data.get('item_name')
		if not item_name:
			raise forms.ValidationError('This field is required')
		return item_name

	def clean_price(self):
		price = self.cleaned_data.get('price')
		if not price:
			raise forms.ValidationError('This field is required')
		return price


class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name', 'barcode']

class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'item_name', 'barcode', 'price', 'quantity']



class StockSaleForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'item_name', 'price', 'sold_quantity', 'sold_to', 'sold_quantity']