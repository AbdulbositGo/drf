from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from api.serializers import UserPublicSerializers

class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    url_update = serializers.HyperlinkedIdentityField("product-update", lookup_field='pk')
    user = UserPublicSerializers(read_only=True)

    class Meta:
        model = Product
        fields = [
            'user',
            'pk',
            'url',
            'url_update',
            # 'email',
            "title",
            "content",
            "price",
            'sale_price',
            'my_discount',
        ]
    # def get_user(self, obj):
    #     return obj.user.username

    # def validate_title(self, value):
    #     if Product.objects.filter(title__iexact=value).exists():
    #         raise serializers.ValidationError(f"{value} is alredy a title name")
    #     return value

    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return f"/api/products/{obj.pk}"
        return reverse('product-detail', kwargs={'pk': obj.pk}, request=request)
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None

        return obj.get_discount()
