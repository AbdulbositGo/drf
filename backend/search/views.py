from rest_framework import generics
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from . import client


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        result = client.perform_search(request.GET.get('q')) 
        if not result:
            return Response('', status=400)   
        return Response(result)


class SearchListOldView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        result = Product.objects.none()
        if q is not None: 
            user = None
            if self.request.user.is_authenticated:
                user =  self.request.user
            result = qs.search(q, user=user)
        return result
    