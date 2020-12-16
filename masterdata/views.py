from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView
from .models import Customer, Meteringpoint
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    paginate_by = 2


class CustomerDetailView(LoginRequiredMixin, SingleObjectMixin, ListView):
    template_name = 'masterdata/customer_detail.html'

    def get(self, requst, *args, **kwargs):
        self.object = self.get_object(queryset=Customer.objects.filter(id=self.kwargs.get('pk')))
        return super().get(requst, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['customer'] = self.object
        return context

    def get_queryset(self):
        return self.object.meteringpoint.all()


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('masterdata:customer-list')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = "__all__"