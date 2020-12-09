from django.urls import path
from . import views

app_name = 'faq'

urlpatterns = [
    path('', views.faq_list, name='faq-list'),
    path('detail/<int:pk>', views.faq_detail, name='faq-detail'),
]
