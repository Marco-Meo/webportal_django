from django.shortcuts import render
from .models import Faq


def faq_list(request):
    faqs = Faq.objects.all()
    return render(request, 'faq/index.html', {'faqs': faqs})

def faq_detail(request, pk):
    faq = Faq.objects.get(id=pk)
    return render(request, 'faq/faq_detail.html', {'faq': faq})