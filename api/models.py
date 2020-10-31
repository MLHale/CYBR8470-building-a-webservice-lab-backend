from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

class Breed(models.Model):
    name = models.CharField(max_length=100, blank=False)
    SIZE_CHOICES = (('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'))
    size = models.CharField(max_length=100, choices=SIZE_CHOICES, blank=False)
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    sheddingamount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)
    exerciseneeds = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=False)

class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')

class Dog(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(validators=[MinValueValidator(0)])
    # breed = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=100, blank=False)
    color = models.CharField(max_length=100, blank=False)
    favoritefood = models.CharField(max_length=100, blank=False)
    favoritetoy = models.CharField(max_length=100, blank=False)
    dogbreed = models.ForeignKey(Breed, default='', blank=False)

class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'name')
