from django.db import models

class Post(models.Model):
    traveler = models.ForeignKey("Traveler", on_delete=models.CASCADE)
    img = models.URLField(max_length=1000)
    title = models.CharField(max_length=50)
    body = models.TextField()
    categories = models.ManyToManyField("Category", through="PostCategory")