from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from apps.shared.models import (
    CommonTimeStampModel,
    CommonUserModel
)


class UserProfile(CommonTimeStampModel, CommonUserModel):
    seacret_room = models.BooleanField(default=False)

    def __str__(self):
        return f'UserProfile: {self.user.username}'

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
        UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_user_profile, sender=User)
