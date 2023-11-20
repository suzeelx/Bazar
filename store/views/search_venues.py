from django.shortcuts import render, redirect
from store.models.product import Products

from django.views import View

class search_venues(View):
    def search_venues(self, request):
    

        return render(request, 'search_venues.html', {})


