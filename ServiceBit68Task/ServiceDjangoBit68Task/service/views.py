from .forms import ProductForm, CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Products
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('products')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
            print(user)
        except:
            messages.error(request, 'email does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('products')

        else:
            messages.error(request, 'user OR password is incorrect')

    return render(request, 'products/login-reg.html')



def logoutPage(request):
    logout(request)
    messages.error(request, ' user logged out')
    return redirect('login')


def registerPage(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            messages.success(request, 'user created')
            login(request, user)
            return redirect('products')
        else:
          messages.error(request, 'an error happened')
    context = { 'page':page, 'form':form}
    return render(request, 'products/login-reg.html', context) 





login_required(login_url='login')
def products(request):
    products = Products.objects.all().order_by('-price')

    # Keep That :- 
    '''
    when you make products = Products.objects.all().order_by('-price')
    ==> It displays all products with their uses 
    if you add filter(user=request.user)
    ==> it will display only user when is login.
    '''
    context = {'products':products}
    return render(request, 'products/products.html', context)



login_required(login_url='login')
def product(request, pk):
    productObj = Products.objects.get(id=pk)
    context = { 'projectObj':productObj}
    return render(request, 'products/single-product.html', context)



login_required(login_url='login')
def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request, 'products/product_form.html', context)


login_required(login_url='login')
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


login_required(login_url='login')
def deleteProduct(request, pk):
    product = Products.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    context = {'product':product}
    return render(request, 'products/delete_product.html', context)
