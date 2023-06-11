from rest_framework import serializers  # Import the serializers from rest_framework
from .models import ChatGPT  # Import the ChatGPT model from chatgpt/models.py
from .models import ApplicationSettings


class ChatGPTSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatGPT
        fields = "__all__"


class ApplicationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationSettings
        fields = "__all__"
