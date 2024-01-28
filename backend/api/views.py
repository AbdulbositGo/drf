from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?")
    products = {}
    if model_data:
        for product in model_data:
            products[f'Product {product.id}'] =  model_to_dict(model_data.first())
    data = {'products': products}
    
    return JsonResponse(data)