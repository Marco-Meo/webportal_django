# Schulung Django Webframework
## Setup

### 1. Downlaod Git Repository

[Github.com]('https://github.com/Marco-Meo/webportal_django.git')

Ausführen im CMD:

`git clone https://github.com/Marco-Meo/webportal_django.git`


### 2. Django Library installieren

`pip install django`

### 3. Datenbank erzeugen

`python manage.py migrate`

### 4. Superuser erstellen

`python manage.py createsuperuser`

### 5. App erstellen

`python manage.py startapp faq`

### 6. App registrieren

settings.py -> 
```
INSTALLED_APPS = [
    ...
    'faq',
]
```

### 7. URL bekannt machen
webportal/urls.py
```
urlpatterns = [
    ...
    path('faq/', include('faq.urls')),
]
```

### 8. Neue Datei urls.py im App faq hinzufügen

```
from django.urls import path
from . import views

app_name = 'faq'

urlpatterns = [
    path('', views.index, name='index'),
]
```

### 9. View erstellt
View im app faq (views.py) erstellen

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("FAQ")
```

### 10. Ordner für HTML Templates erstellen
faq/Templates/faq

### 11. HTML Template Datei erstellen
Im oben erstellen Ordner die Datei index.html erstellen.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FAQ</title>
</head>
<body>
    <h1>FAQ</h1>
</body>
</html>
```

### 12. Datenbank Modell erstellen
faq/models.py

```
from django.db import models

class Faq(models.Model):
    title = models.CharField('Titel', max_length=200)
    description = models.CharField('Beschreibung', max_length=1000)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.title

```

### 13. Model für Backend registrieren
faq/admin.py

```
from django.contrib import admin
from . import models

admin.site.register(models.Faq)
```

### 14. Anzeige der FAQ Liste, Update und Detail
Neue Funktion faq_list erstellen

faq/views.py
```
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

```

faq/urls.py erweitern
```
urlpatterns = [
    path('', views.faq_list, name='faq-list'),
    path('detail/<int:pk>', views.faq_detail, name='faq-detail'),
    path('detail/<int:pk>/update', views.faq_update, name='faq-update'),
]
```

Template faq/index.html anpassen
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FAQ</title>
</head>
<body>
    <h1>FAQ</h1>
    <ul>
        {% for faq in faqs %}
        <li>
            {{ faq.title }} (<a href="{% url 'faq:faq-detail' faq.id %}">Detail</a>
             | <a href="{% url 'faq:faq-update' faq.id %}">Edit</a>)
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

Template faq/faq_detail.html erstellen

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FAQ Eintrag</title>
</head>
<body>
    <h2>{{ faq.title }}</h2>
    <p>{{ faq.description }}</p>
    </br>
    Ersteller: {{ faq.creator }} @ {{ faq.creation_date | date:"d.M.Y h:m"}}
</body>
</html>
```

Template faq/faq_update.html erstellen

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FAQ editieren</title>
</head>
<body>
    <h2>Editiere FAQ Eintrag</h2>

    <div>
        <form action="" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Speichern">
        </form>
    </div>
</body>
</html>
```

### 15. Neuer FAQ Eintrag erstellen

Neues html template erstellen faq/templates/faq_create.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FAQ Eintrag erstellen</title>
</head>
<body>
    <h2>FAQ Eintrag erstellen</h2>

    <div>
        <form action="" method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Speichern">
        </form>
    </div>
</body>
</html>
```

faq/views.py erweitern um Funktion

```
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def faq_create(request):
    form = FaqForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            faq_form = form.save(commit=False)
            faq_form.creator = request.user
            form.save()
            return redirect('faq:faq-list')
    return render(request, 'faq/faq_create.html', {'form': form})
```

urls.py erweitern

```
urlpatterns = [
    ...
    path('create/', views.faq_create, name='faq-create'),
]
```

index.html erweitern

```
<div>
    {% if user.is_authenticated %}
        <a href="{% url 'faq:faq-create' %}">Neuer Eintrag erstellen</a>
    {% endif %}
</div>
```

### 16. FAQ Eintrag löschen
Neue View erstellen faq/views.py

```
@login_required(login_url='/admin/login')
def faq_delete(request, pk):
    if request.method == 'GET':
        faq = get_object_or_404(Faq, pk=pk)
        faq.delete()
    return redirect('faq:faq-list')
```

Neuer Eintrag in urls.py

```
urlpatterns = [
    ...
    path('detail/<int:pk>/delete', views.faq_delete, name='faq-delete'),
]
```

Index.html erweitern

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FAQ</title>
</head>
<body>
    <h1>FAQ</h1>
    <ul>
        {% for faq in faqs %}
        <li>
            {{ faq.title }} (<a href="{% url 'faq:faq-detail' faq.id %}">Detail</a>
             | <a href="{% url 'faq:faq-update' faq.id %}">Edit</a>
            | <a href="{% url 'faq:faq-delete' faq.id %}">Löschen</a>)
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Django Rest Framework

### 1. Setup

```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter 
```

Installed Apps in webportal/settings.py
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

```
# Thirdparty configuration
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissions',
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}
```

Eintrag in webportal/urls.py

```
# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
]
```

### 2. API-Router erstellen
Datei webportal/api_router.py erstellen:

```
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from faq.api.views import FaqViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("faq", FaqViewSet)


app_name = "api"
urlpatterns = router.urls
```

### 3. Serializer und view erstellen

Ordner "api" im App Ordner faq erstellen

Datei serializer.py im Ordner api erstellen

```
from rest_framework import serializers
from masterdata.models import Faq

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"
        extra_kwargs = {
            "url": {"view_name": "api:faq-detail"}
        }

```

Datei views.py im Ordner api erstellen:
```
from masterdata.models import Faq
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import FaqSerializer


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    queryset = Faq.objects.all()
    permission_classes = [permissions.IsAuthenticated]
```