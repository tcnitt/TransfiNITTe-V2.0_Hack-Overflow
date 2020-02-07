from .models import Vehicle
from rest_framework import serializers


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['car_no','entry_time','exit_time','car_model']



