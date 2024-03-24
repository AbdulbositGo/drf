from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializers


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    date = {}
    if instance:
        # data = model_to_dict(
        #     instance.first(), fields=["id", "title", "content", "price", "sale_proce"]
        # )
        data = ProductSerializers(instance).data
    return Response(data)   
