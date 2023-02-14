import uuid as uuid
from django.db import models

from products.models import Product
from statuses.models import Status


class Cart_item(models.Model):
    uuid = models.UUIDField(
        'uuid',
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField(
        default=0
    )
    status_id = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )
    user_rating = models.DecimalField(
        default=5,
        max_digits=2,
        decimal_places=1,
        blank=True,
        null=True
    )
    actual_data = models.DateTimeField()
    # user_id = models.ForeignKey()

