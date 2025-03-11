from django.urls import path # import to define URL patterns
from .views import StoreListCreateView, StoreDetailView # import API views for handling store-related requests

urlpatterns = [
    path('api/stores/', StoreListCreateView.as_view(), name='store-list-create'), # endpoint at 'api/stores', maps it to StoreListCreateView for listing and creating
    path('api/stores/<int:id>/', StoreDetailView.as_view(), name='store-detail'), # endpoint at 'api/stores/<id>', maps it to StoreDetailView for retrieving, updating or deleting
]
