from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

class blogsearchview(View):
	def get_queryset(self):
		query=self.request.GET.get('q')
		return Products.objects.filter(name__icontains=query)


