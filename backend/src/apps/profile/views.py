import logging

from rest_framework import viewsets
from rest_framework.response import Response

from apps.profile.permissions import (
    JSONWebTokenAuthentication
)
from .serializers import ProfileSerializer

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfileSet(viewsets.GenericViewSet):
    name = 'user-profile'
    lookup_field = 'user'
    authentication_classes = [
        JSONWebTokenAuthentication
    ]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return self.request.user.profile

    def list(self, *args, **kwargs):
        return Response(ProfileSerializer(self.get_queryset()).data)
