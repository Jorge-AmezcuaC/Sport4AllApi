from rest_framework import serializers
from . import models

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrecioH
        fields = '__all__'