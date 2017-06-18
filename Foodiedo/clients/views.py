from django.shortcuts import render, get_list_or_404

from .models import Product

def index(request):
    products = get_list_or_404(Product)
    template = 'clients/index.html'
    context = {'products': products}
    return render(request, template, context)
