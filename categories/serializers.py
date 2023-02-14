from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('uuid',
                  'name',
                  'description',
                  )
        extra_kwargs = {
            'uuid': {'validators': []},
        }