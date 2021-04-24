from django.db import models
from django.utils import timezone

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    body = models.TextField(max_length=350)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.summary