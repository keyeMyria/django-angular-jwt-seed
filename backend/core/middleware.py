from urllib.parse import parse_qs

import jwt
from channels.auth import AuthMiddlewareStack
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from django.utils.translation import ugettext as _
from rest_framework import exceptions
from rest_framework_jwt.authentication import jwt_decode_handler, jwt_get_username_from_payload


class JWTAuthMiddleware():
    """
    Token authorization middleware for Django Channels 2
    """

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):

        query_dict = {k: v[0] for k, v in parse_qs(scope["query_string"].decode()).items()}

        jwt_value = query_dict.get('token', None)
        if jwt_value:
            try:
                try:
                    payload = jwt_decode_handler(jwt_value)
                except jwt.ExpiredSignature:
                    msg = _('Signature has expired.')
                    raise exceptions.AuthenticationFailed(msg)
                except jwt.DecodeError:
                    msg = _('Error decoding signature.')
                    raise exceptions.AuthenticationFailed(msg)
                except jwt.InvalidTokenError:
                    raise exceptions.AuthenticationFailed()

                scope['user'] = self.authenticate_credentials(payload)

            except exceptions.AuthenticationFailed:
                scope['user'] = AnonymousUser()

        return self.inner(scope)

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        User = get_user_model()
        username = jwt_get_username_from_payload(payload)

        if not username:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            msg = _('Invalid signature.')
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)

        close_old_connections()
        return user


JWTAuthMiddlewareStack = lambda inner: JWTAuthMiddleware(AuthMiddlewareStack(inner))
