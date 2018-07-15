import logging

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import UserSerializer

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ProfileView(viewsets.GenericViewSet):
    name = 'user-profile'
    lookup_field = 'user'
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset())
        return Response(serializer.data)
