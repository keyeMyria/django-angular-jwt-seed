from rest_framework import viewsets, views, generics
from rest_framework.response import Response

from profile_module.permissions import (
    IsAuthenticated,
    SessionAuthentication,
    BasicAuthentication,
    JSONWebTokenAuthentication,
    IsOwnerOnly
)
from .serializers import ProfileSerializer
import logging

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
