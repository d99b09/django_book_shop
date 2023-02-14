from rest_framework import serializers

from cart_items.models import Cart_item
from products.models import Product
from statuses.models import Status


class Cart_itemSerializer(serializers.ModelSerializer):
    product_id = serializers.SlugRelatedField(
        slug_field="uuid",
        queryset=Product.objects.all(),
        allow_null=False,
        required=False
    )
    # user_id = serializers.SlugRelatedField(
    #     slug_field="uuid",
    #     queryset=Userprofile.objects.all(),
    #     allow_null=True,
    #     required=False
    # )
    status_id = serializers.SlugRelatedField(
        slug_field="uuid",
        queryset=Status.objects.all(),
        allow_null=False,
        required=False
    )

    class Meta:
        model = Cart_item
        fields = (
            'uuid',
            'product_id',
            'quantity',
            'status_id',
            'user_rating',
            'actual_data'
        )
        extra_kwargs = {
            'uuid': {'validators': []},
        }