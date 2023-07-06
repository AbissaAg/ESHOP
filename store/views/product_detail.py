from django.shortcuts import render, get_object_or_404
from django.http import Http404
from store.models import Products

def product_detail(request, id):
    try:
        product = get_object_or_404(Products, id=id)
    except Products.DoesNotExist:
        raise Http404("Product does not exist")
    
    context = {'product': product}
    return render(request, 'product_detail.html', context)
