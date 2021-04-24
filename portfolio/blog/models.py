from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    body = models.TextField(max_length=350)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.summary


#add blog app into setting, url, views, html

#title  CharField
#pub_date  DateTimeField
#body  TextField
#image  ImageField

#makemigrations
#migrate
#add to admin
#def __str__

#update views
#update allblog.html