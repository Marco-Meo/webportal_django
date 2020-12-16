from django.urls import path
from . import views

app_name = 'masterdata'

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.CustomerListView.as_view(), name="customer-list"),
    path('customer/<int:pk>/detail', views.CustomerDetailView.as_view(), name="customer-detail"),
    path('customer/<int:pk>/delete', views.CustomerDeleteView.as_view(), name="customer-delete"),
    path('customer/<int:pk>/update', views.CustomerUpdateView.as_view(), name="customer-update"),
]
