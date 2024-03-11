from rest_framework import serializers
from .models import *
class remind_serializer(serializers.Serializer):
    class Meta:
        model=remind_user
        fileds='__all__'