from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ItemGroup (models.Model):
    pass

class Item (models.Model):

    name = models.CharField()
    creation_date = models.DateField()
    arrival_date = models.DateField()
