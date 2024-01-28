from django.shortcuts import render
from django.http import JsonResponse
import json
from products.models import Product


def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?")
    products = {}
    if model_data:
        for i in model_data:
            products[f'Product {i.id}'] = {
                "id": i.id,
                'title': i.title,
                'content': i.content,
                'price': i.price
            }
    data = {'products': products}
    
    return JsonResponse(data)