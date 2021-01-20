from rest_framework import serializers

from .models import AZS, Statistics

class AZSSerializer(serializers.ModelSerializer):
    class Meta:
        model = AZS
        fields = '__all__'
