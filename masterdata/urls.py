from django.urls import path
from . import views

app_name = 'masterdata'

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.CustomerListView.as_view(), name="customer-list"),
    path('/customer/<int:pk>/detail', views.CustomerDetailView.as_view(), name="customer-detail"),
]
