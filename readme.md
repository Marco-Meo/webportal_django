# Schulung Django Webframwork
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
