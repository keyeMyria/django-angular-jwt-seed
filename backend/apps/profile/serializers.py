from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ['id']
        read_only_fields = ['user']


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False, read_only=True)
    date_joined = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False, read_only=True)
    userprofile = serializers.SerializerMethodField()

    sidemenu = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        exclude = [
            'password',
            'id',
        ]

    def get_userprofile(self, object):
        return ProfileSerializer(object.userprofile_set).data

    def get_sidemenu(self, inst):
        sidemenu_group = [{
            'group_icon': 'dashboard',
            'group_name': 'dashboard',
            'group_list': [
                {
                    'route': '/dashboard',
                    'name': 'User',
                    'icon': 'user'
                }
            ]
        }]

        if inst.userprofile_set.get().seacret_room:
            menu_item = {
                'group_icon': 'map-marker',
                'group_name': 'secret',
                'group_list': [
                    {
                        'route': '/secret/component',
                        'name': 'secret',
                        'icon': 'view-cards'
                    },
                ]
            }

            sidemenu_group.append(menu_item)
        return sidemenu_group
