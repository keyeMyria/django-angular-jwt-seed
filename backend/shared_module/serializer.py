from rest_framework import serializers
from django_celery_results.models import TaskResult


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
