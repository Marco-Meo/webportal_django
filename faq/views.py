from django.shortcuts import render
from .models import Faq


def faq_list(request):
    faqs = Faq.objects.all()
    return render(request, 'faq/index.html', {'faqs': faqs})