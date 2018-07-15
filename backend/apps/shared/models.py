from django.contrib.auth.models import User
from django.db import models
from django_celery_results.models import TaskResult


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


class CommonUserModel(models.Model):
    """ Owner table abstract """

    user = models.ForeignKey(
        User,
        default=None,
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class CommonCeleryResultsModel(models.Model):
    """ Celery table abstract """

    task = models.OneToOneField(
        TaskResult,
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    task_log = models.TextField(
        blank=True,
        null=True,
        default=None
    )

    class Meta:
        abstract = True
