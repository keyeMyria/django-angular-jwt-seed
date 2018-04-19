from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from shared.models import (
    CommonTimeStampModel
)


class UserProfile(CommonTimeStampModel):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name=('profile'),
        on_delete=models.CASCADE,
        verbose_name=("profile"),
    )

    def __str__(self):
        return f'UserProfile: {self.owner.username}'

    class Meta:
        ordering = ['-id']


def create_user_profile(sender, **kwargs):
    """
    create_user_profile for each created user
    :param sender:
    :param kwargs:
    :return:
    """

    if kwargs['created']:
        UserProfile.objects.create(owner=kwargs['instance'])


post_save.connect(create_user_profile, sender=User)
