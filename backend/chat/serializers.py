from rest_framework.serializers import ModelSerializer
from .models import *


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
