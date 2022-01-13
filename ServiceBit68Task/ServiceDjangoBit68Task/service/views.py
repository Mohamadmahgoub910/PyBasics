from .forms import ProductForm
from django.shortcuts import render
from .models import Products
# Create your views here.

def products(request):
    products = Products.objects.all().order_by('-price')
    context = {'products':products}
    return render(request, 'products/products.html', context)

def product(request, pk):
    productObj = Products.objects.get(id=pk)
    context = { 'projectObj':productObj}
    return render(request, 'products/single-product.html', context)

def createProduct(request):
    form = ProductForm()
    context = {'form':form}
    return render(request, 'products/product_form.html', context)