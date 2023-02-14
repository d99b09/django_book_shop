from rest_framework import serializers

from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('uuid',
                  'name',
                  'description',
                  'portrait',
                  'berth_data',
                  'death_data',

                  )
        extra_kwargs = {
            'uuid': {'validators': []},
        }