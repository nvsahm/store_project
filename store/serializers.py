from rest_framework import serializers 
from .models import Store 

class StoreSerializer(serializers.ModelSerializer): # define a serzializer for the Store model
    class Meta:
        model = Store # specify that the serializer is for the Store model
        fields = ['id', 'store_name', 'address', 'opening_hours'] # define which fields should be included in the serialized output
