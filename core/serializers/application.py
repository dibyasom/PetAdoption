from rest_framework import serializers

# Model
from core.models.application import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["pet", "email", "reason"]
