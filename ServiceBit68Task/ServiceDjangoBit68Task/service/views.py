from .forms import ProductForm, CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Products
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from service.serializers import ProductSerializer, UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import status

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
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'user created')
            login(request, user)
            return redirect('products')
        else:
            messages.error(request, 'an error happened')
    context = {'page': page, 'form': form}
    return render(request, 'products/login-reg.html', context)


@api_view(['POST'])
def registerUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['first_name'],
            email=data['email'],
            password=make_password(data['password'])
        )

        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUserById(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
# login_required(login_url='login')
def products(request):
    products = Products.objects.all().order_by('-price')

    # Keep That :-
    '''
    when you make products = Products.objects.all().order_by('-price')
    ==> It displays all products with their uses 
    if you add filter(user=request.user)
    ==> it will display only user when is login.
    '''
    serializer = ProductSerializer(products, many=True)
    # context = {'products': products}
    # return render(request, 'products/products.html', context)
    return Response(serializer.data)


# login_required(login_url='login')
@api_view(['GET'])
def product(request, pk):
    productObj = Products.objects.get(id=pk)
    serializer = ProductSerializer(productObj, many=False)
    # context = {'projectObj': productObj}
    # return render(request, 'products/single-product.html', context)
    return Response({'productById': serializer.data})


# login_required(login_url='login')
@api_view(['POST'])
def createProduct(request):
    # form = ProductForm()
    # if request.method == 'POST':
    #     form = ProductForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('products')
    # context = {'form': form}
    # return render(request, 'products/product_form.html', context)

    # user = request.user
    # he must log in first to make sure who is this user so i hashed them first
    product = Products.objects.create(
        # user=user,
        name='Sample Name',
        price=0,
    )
    serializer = ProductSerializer(product, many=True)
    return Response('Product created', serializer.data)


# login_required(login_url='login')
@api_view(['PUT'])
def updateProduct(request, pk):
    data = request.data
    product = Products.objects.get(id=pk)
    # form = ProductForm(instance=product)
    # if request.method == 'POST':
    #     form = ProductForm(request.POST, instance=product)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('products')
    # context = {'form': form}
    # return render(request, 'products/product_form.html', context)
    product.name = data['name']
    product.price = data['price']
    product.save()
    serializer = ProductSerializer(product, many=False)
    return Response('Product updated', serializer.data)


# login_required(login_url='login')
@api_view(['DELETE'])
def deleteProduct(request, pk):
    # product = Products.objects.get(id=pk)
    # if request.method == 'POST':
    #     product.delete()
    #     return redirect('products')
    # context = {'product': product}
    # return render(request, 'products/delete_product.html', context)
    product = Products.objects.get(id=pk)
    product.delete()
    return Response('Product Deleted')
