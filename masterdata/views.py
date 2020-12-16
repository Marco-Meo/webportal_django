from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Customer, Meteringpoint

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")


class CustomerListView(ListView):
    model = Customer