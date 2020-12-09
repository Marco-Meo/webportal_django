from django.urls import path
from . import views

app_name = 'masterdata'

urlpatterns = [
    path('', views.index, name='index'),
]
