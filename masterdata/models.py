from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Utility(models.Model):
    company_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.company_name



class Customer(models.Model):
    company_name = models.CharField("Firma", max_length=100)
    street = models.CharField("Strasse", max_length=100, help_text="Strasse und Strassennummer")
    zip = models.CharField("PLZ", max_length=4)
    city = models.CharField("Ort", max_length=60)


    def __str__(self):
        return self.company_name

class Meteringpoint(models.Model):
    meteringcode = models.CharField("Messpunktnummer", max_length=33, validators=[MinLengthValidator(33),])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.meteringcode