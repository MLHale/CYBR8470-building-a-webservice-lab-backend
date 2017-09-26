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

class Dog(models.Model):
        #name (a character string)
        name = models.CharField(max_length=100)
        #age (an integer)
        age = models.IntegerField(max_length=2)
        #breed (a foreign key to the Breed Model)
        breed = models.ForeignKey('Breed')
        #gender (a character string)
        gender = models.CharField(max_length=1)
        #color (a character string)
        color = models.CharField(max_length=20)
        #favoritefood (a character string)
        favoritefood = models.CharField(max_length=30)
        #favoritetoy (a character string)
        favoritetoy = models.CharField(max_length=30)

        def __str__(self):
            return str(self.name)

class Breed(models.Model):

        #name (a character string)
        name = models.CharField(max_length=100)
        #size (a character string) [should accept Tiny, Small, Medium, Large]
        TINY = 'TINY'
        SMALL = 'SMALL'
        MEDIUM = 'MEDIUM'
        LARGE = 'LARGE'
        SIZE_CHOICES = (
            (TINY, 'Tiny'),
            (SMALL, 'Small'),
            (MEDIUM, 'Medium'),
            (LARGE, 'Large'),
        )
        size = models.CharField(max_length=6, choices=SIZE_CHOICES)
        #friendliness (an integer field) [should accept values from 1-5]
        friendliness = models.IntegerField(max_length=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
        #trainability (an integer field) [should accept values from 1-5]
        trainability = models.IntegerField(max_length=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
        #sheddingamount (an integer field) [should accept values from 1-5]
        sheddingamount = models.IntegerField(max_length=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
        #exerciseneeds (an integer field) [should accept values from 1-5]
        exerciseneeds = models.IntegerField(max_length=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return str(self.name) + str(self.size) + str(self.friendliness) + str(self.trainability) + str(self.sheddingamount) + str(self.exerciseneeds)
