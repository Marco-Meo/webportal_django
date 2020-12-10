from django.shortcuts import render, get_object_or_404, redirect
from .models import Faq
from .forms import FaqForm

def faq_list(request):
    faqs = Faq.objects.all()
    return render(request, 'faq/index.html', {'faqs': faqs})


def faq_detail(request, pk):
    faq = get_object_or_404(Faq, pk=pk)
    return render(request, 'faq/faq_detail.html', {'faq': faq})


def faq_update(request, pk):
    faq = get_object_or_404(Faq, pk=pk)
    form = FaqForm(request.POST or None, instance=faq)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('faq:faq-list')

    return render(request, 'faq/faq_update.html', {'form': form})


def faq_create(request):
    form = FaqForm(request.POST or None)

    return render(request, 'faq/faq_create.html', {'form': form})