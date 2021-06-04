from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=150)
    surname_1 = models.CharField(max_length=50, blank=True, null=True)
    surname_2 = models.CharField(max_length=50, blank=True, null=True)


class ContactSubtype(models.Model):
    name = models.CharField(max_length=50)
