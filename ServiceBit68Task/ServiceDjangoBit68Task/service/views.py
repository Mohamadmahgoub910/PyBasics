from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def products(request):
    return HttpResponse("Hello From Products ")

def product(request, pk):
    return HttpResponse('Single product' + ' ' + str(pk) )
