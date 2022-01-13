from .forms import ProductForm
from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request, 'products/product_form.html', context)

def updateProduct(request, pk):
    product = Products.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request, 'products/product_form.html', context)

def deleteProduct(request, pk):
    product = Products.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {'product':product}
    return render(request, 'products/delete_product.html', context)
