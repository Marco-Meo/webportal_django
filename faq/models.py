from django.db import models

class Faq(models.Model):
    title = models.CharField('Titel', max_length=200)
    description = models.CharField('Beschreibung', max_length=1000)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.title
