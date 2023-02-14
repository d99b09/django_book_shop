import uuid as uuid
from django.db import models

from authors.models import Author
from categories.models import Category


# Create your models here.
class Product(models.Model):
    uuid = models.UUIDField(
        'uuid',
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=100, db_index=True)
    description = models.TextField(
        blank=True,
        null=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    stock = models.PositiveIntegerField(
        default=0
    )
    categories_ids = models.ManyToManyField(
        Category,
        # blank=True,
        # null=True,
    )
    rating = models.DecimalField(
        default=5,
        max_digits=2,
        decimal_places=1,
        blank=True,
        null=True
    )
    author_id = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    date = models.IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name