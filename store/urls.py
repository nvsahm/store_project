from django.urls import path 
from .views import StoreListCreateView, StoreDetailView 

urlpatterns = [
    path('api/stores/', StoreListCreateView.as_view(), name='store-list-create'), # endpoint at 'api/stores', maps it to StoreListCreateView 
    path('api/stores/<int:id>/', StoreDetailView.as_view(), name='store-detail'), # endpoint at 'api/stores/<id>', maps it to StoreDetailView 
]
