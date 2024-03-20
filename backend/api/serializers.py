from rest_framework import serializers

from products.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "content", "price"]