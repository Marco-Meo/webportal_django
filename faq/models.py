from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Faq(models.Model):
    title = models.CharField('Titel', max_length=200)
    description = models.CharField('Beschreibung', max_length=1000)
    creation_date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.title
