import uuid as uuid
from django.db import models


class Status(models.Model):
    uuid = models.UUIDField(
        'uuid',
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    status_name = models.CharField(
        max_length=100, db_index=True)

    def __str__(self):
        return self.status_name
