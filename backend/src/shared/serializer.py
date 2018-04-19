from django_celery_results.models import TaskResult
from rest_framework import serializers


class TaskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = [
            'id',
            'task_id',
            'status'
        ]
        read_only_fields = [
            'id',
            'task_id',
            'status'
        ]
