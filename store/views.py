from django.shortcuts import render
from .models import Store
from .serializers import StoreSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .filters import StoreFilter  # Import the StoreFilter class

class StoreListCreateView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['store_name', 'address']
    filterset_class = StoreFilter

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('store_name', openapi.IN_QUERY, description='Filter by store name', type=openapi.TYPE_STRING, required=False),
            openapi.Parameter('address', openapi.IN_QUERY, description='Filter by address', type=openapi.TYPE_STRING, required=False),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


# Retrieve, Update, and Delete a Store by ID (GET, PUT, DELETE)
class StoreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()  # Retrieve all Store objects.
    serializer_class = StoreSerializer  # Use StoreSerializer for JSON conversion.
    authentication_classes = [TokenAuthentication]  # Require token authentication.
    permission_classes = [IsAuthenticated]  # Only authenticated users can access.
    lookup_field = "id"  # Specify that the object lookup should be done using "id" instead of "pk".
