from rest_framework import serializers
from .models import servers


class updates(serializers.ModelSerializer):
  class Meta:
    model = servers
    fields = '__all__'