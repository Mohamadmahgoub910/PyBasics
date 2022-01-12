from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def products(request):
    return render(request, 'products/products.html')

def product(request, pk):
    return render(request, 'products/single-product.html')
