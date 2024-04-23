from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    url_update = serializers.HyperlinkedIdentityField('product-update', lookup_field='pk')
    
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'user',
            'pk',
            'url',
            'url_update',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
        ]

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return f'/api/products/{obj.pk}'
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.get_discount()
