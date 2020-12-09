from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("FAQ")
    var = {}
    return render(request, 'faq/index.html', var)