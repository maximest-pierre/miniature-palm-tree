from __future__ import unicode_literals

from django.db import models


class ItemGroup (models.Model):
    pass


class Item (models.Model):

    name = models.CharField(max_length=150)
    creation_date = models.DateField()
    arrival_date = models.DateField()
