import uuid as uuid
from django.db import models


class Category(models.Model):
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
        default=''
    )

    def __str__(self):
        return self.name