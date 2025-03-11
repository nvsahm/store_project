from rest_framework import serializers # import Django REST Framework's seriazilizers module
from .models import Store # import Store model from current app's model

class StoreSerializer(serializers.ModelSerializer): # define a serzializer for the Store model
    class Meta:
        model = Store # specify that the serializer is for the Store model
        fields = ['id', 'store_name', 'address', 'opening_hours'] # define which fields should be included in the serzialized output
