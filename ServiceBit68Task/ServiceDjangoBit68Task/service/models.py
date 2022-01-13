from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField( max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    createdAt = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name
