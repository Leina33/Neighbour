from __future__ import unicode_literals
import numpy as np
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.db.models.sql.datastructures import Join
# Create your models here.

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()
        
class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name