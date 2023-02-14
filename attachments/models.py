import uuid as uuid
from django.db import models

from products.models import Product


# Create your models here.
class Attachment(models.Model):
    uuid = models.UUIDField(
        'uuid',
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    file_path = models.ImageField(
        upload_to='uploads/%Y/%m/%d/'#TODO
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
