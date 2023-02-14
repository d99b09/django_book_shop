from rest_framework import serializers

from authors.models import Author
from categories.models import Category
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    author_id = serializers.SlugRelatedField(
        slug_field="uuid",
        queryset=Author.objects.all(),
        allow_null=True,
        required=False
    )
    categories_ids = serializers.SlugRelatedField(
        slug_field="uuid",
        required=False,
        many=True,
        queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = ('uuid',
                  'name',
                  'description',
                  'price',
                  'stock',
                  'categories_ids',
                  'rating',
                  'author_id',
                  'date'
                  )
        extra_kwargs = {
            'uuid': {'validators': []},
        }