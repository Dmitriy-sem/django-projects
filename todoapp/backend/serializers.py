from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('pk', 'title', 'is_done')
