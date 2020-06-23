from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from .forms import StockCreateForm, StockSearchForm, StockUpdateForm, StockSaleForm
# Create your views here.
def index(request):
	queryset = Setting.objects.all()
	setting = Setting.objects.get()

	context = {'setting':setting, 'queryset':queryset,}
	return render(request, 'index.html', context)


def about(request):
	queryset = Setting.objects.all()
	setting = Setting.objects.get()

	context = {'setting':setting, 'queryset':queryset,}
	return render(request, 'index.html', context)

def features(request):
	queryset = Setting.objects.all()
	setting = Setting.objects.get()

	context = {'setting':setting, 'queryset':queryset,}
	return render(request, 'features.html', context)


def inventory(request):
	title = 'List of Items'
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	stock = Stock.objects.filter()
	stock = Stock.objects.filter()
	sold_total=0
	for instance in stock:
		sold_total += instance.sold_quantity


	context = {
		"title":title, "queryset":queryset, "form":form, "sold_total":sold_total
	}

	if request.method == 'POST':
		queryset = Stock.objects.filter(category__icontains=form['category'].value(),
										item_name__icontains=form['item_name'].value(),
										barcode__icontains=form['barcode'].value()
										)
		context = {
		"form": form,
		"title": title,
		"queryset": queryset,
		"amount": amount,
	}
	return render(request, 'inventory.html', context)

def adminsite(request):
	title = 'Admin Check'
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	stock = Stock.objects.filter()
	subtotal=0
	for instance in stock:
		subtotal += instance.sub_total

	maintotal=0
	for instance in stock:
		maintotal += instance.total

	context = {
		"title":title, "queryset":queryset, "form":form, "subtotal":subtotal, "maintotal":maintotal
	}
	return render(request, 'adminsite.html', context)

def add_inventory(request):
	form = StockCreateForm(request.POST or None)

	if form.is_valid():
		form.save()
		messages.success(request, 'Item successfully added')
		return redirect('/inventory')
	context = {
		"form": form,
		"title": "Add New Items",
	}
	return render(request, "add_inventory.html", context)

def sell_inventory(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockSaleForm(instance=queryset)
	if request.method == 'POST':
		form = StockSaleForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/inventory')

	context = {
		'form':form
	}
	return render(request, 'add_inventory.html', context)


def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/inventory')

	context = {
		'form':form
	}
	return render(request, 'add_inventory.html', context)