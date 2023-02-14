import uuid as uuid
from django.db import models


class Author(models.Model):
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
    portrait = models.ImageField(
        blank=True,
        null=True,
    )
    berth_data = models.IntegerField(
        blank=True,
        null=True,
    )
    death_data = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
