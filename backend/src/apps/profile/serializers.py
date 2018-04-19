from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False, read_only=True)
    date_joined = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False, read_only=True)

    class Meta:
        model = User
        exclude = [
            'password',
            'id'
        ]


class ProfileSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        exclude = [
            'id'
        ]
        read_only_fields = (
        )
