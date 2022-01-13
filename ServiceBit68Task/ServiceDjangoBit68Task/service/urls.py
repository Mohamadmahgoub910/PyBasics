from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),

    path('products/', views.products, name='products'),
    path('product/<str:pk>/', views.product, name='product'),
    path('products/createProduct/', views.createProduct, name='product-create'),
    path('products/updateProduct/<str:pk>', views.updateProduct, name='product-update'),
    path('products/deleteProduct/<str:pk>', views.deleteProduct, name='product-delete'),
]