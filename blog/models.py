from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog (models.Model):

    title = models.CharField (max_length = 255)
    description = models.TextField (max_length = 900)
    img = models.ImageField (upload_to= 'blog' , null= True , blank= True)
    date = models.DateTimeField (auto_now_add = True , blank = True , null = True , auto_now = False)
    update_at = models.DateTimeField (auto_now = True , auto_now_add = False ,null = True , blank = True)
    author = models.ForeignKey (User , on_delete = models.CASCADE)

    def __str__ (self):
        return "{}-{}".format (self.title , self.date)

