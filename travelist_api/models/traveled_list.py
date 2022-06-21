from django.db import models

class TraveledList(models.Model):
    location = models.CharField(max_length=25)