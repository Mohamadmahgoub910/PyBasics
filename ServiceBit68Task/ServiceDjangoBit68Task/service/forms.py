from django.forms import ModelForm
from .models import Products
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1', 'password2']
