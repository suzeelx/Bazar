from django.shortcuts import render, redirect
from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from store.models.product import Products
from django.views import  View

def product_list(request):
    query = request.GET.get('q')
    products = Products.objects.all();

    if query:
        products = Products.objects.filter(name__icontains=query)

    return render(request, 'product_list.html', {'products': products})