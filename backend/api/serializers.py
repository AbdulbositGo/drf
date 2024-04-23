from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        'product-detail',
        lookup_field="pk",
        read_only=True
        )


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)

    # def get_other_products(self, obj):
    #     products = obj.product_set.all()[:3]
    #     return UserProductInlineSerializer(products, many=True, context=self.context).data
