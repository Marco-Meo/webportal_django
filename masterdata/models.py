from django.db import models
from django.contrib.auth.models import User


class Utility(models.Model):
    company_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.company_name