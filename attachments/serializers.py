from rest_framework import serializers
from attachments.models import Attachment
from products.models import Product


class AttachmentSerializer(serializers.ModelSerializer):
    file_path = serializers.ImageField(use_url=True)
    product_id = serializers.SlugRelatedField(
        slug_field="uuid",
        queryset=Product.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Attachment
        fields = (
            'uuid',
            'file_path',
            'product_id')
        extra_kwargs = {
            'uuid': {'validators': []},
        }
