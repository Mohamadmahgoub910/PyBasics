from django.forms import ModelForm, fields
from .models import Products



class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = '__all__'