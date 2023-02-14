import uuid as uuid

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    uuid = models.UUIDField(
        'uuid',
        unique=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.OneToOneField(User, related_name='profiles', on_delete=models.CASCADE)
    address = models.TextField(
        blank=True,
        null=True
    )
    cart_number = models.TextField(
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
