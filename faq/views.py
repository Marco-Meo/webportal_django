from django.shortcuts import render, get_object_or_404, redirect
from .models import Faq
from .forms import FaqForm
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='/admin/login/')
def faq_create(request):
    form = FaqForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            faq_form = form.save(commit=False)
            faq_form.creator = request.user
            faq_form.save()
            return redirect('faq:faq-list')

    return render(request, 'faq/faq_create.html', {'form': form})