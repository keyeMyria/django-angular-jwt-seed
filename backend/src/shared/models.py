from django.db import models


class CommonTimeStampModel(models.Model):
    """ Time table abstract """

    created = models.DateTimeField(
        auto_now=False,
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True,
        auto_now_add=False
    )

    class Meta:
        abstract = True
