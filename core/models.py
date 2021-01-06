from django.db import models

# Create your models here.

class ContactModal(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=100)
    sub   = models.CharField(max_length=55)
    msg   = models.CharField(max_length=100)