from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Service (models.Model):

    title = models.CharField (max_length = 255)

    description = models.TextField (max_length = 2500)

    image = models.ImageField (upload_to='media/service')

    date = models.DateTimeField (auto_now_add = True , auto_now = False)

    user = models.ForeignKey (User,on_delete = models.CASCADE)

    def __str__(self):

        return "{}-{}".format (self.date , self.title)