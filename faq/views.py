from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("FAQ")

    liste_1 = ['Hans','Peter','Urs','Werner']

    var = {
        "variable": "123",
        "namen": liste_1
           }

    return render(request, 'faq/index.html', var)