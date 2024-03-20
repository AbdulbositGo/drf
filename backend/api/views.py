from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?")
    products = {}
    if model_data:
        for product in model_data:
            products[f'Product {product.id}'] =  model_to_dict(model_data.first())
    data = {'products': products}
    
    return Response(data)       