from django.db import models

class BucketList(models.Model):
    location = models.CharField(max_length=25)