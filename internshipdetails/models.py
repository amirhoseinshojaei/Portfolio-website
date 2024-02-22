from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Intership (models.Model):
    country_list = [
      ("1","Iran"),
      ("2","England"),
      ("3","USA"),
      ("4","Germanny"),
      ("5","France"),
      ("6","SouthKorea"),
    ]
    full_name = models.CharField (max_length = 255)
    email = models.EmailField()
    college_name = models.CharField(max_length = 255)
    nationality = models.CharField (max_length = 255 , choices = country_list , default = "USA")
    offer_status = models.CharField(max_length = 255)
    start_date = models.DateTimeField (auto_now = True , auto_now_add = False)
    end_date = models.DateTimeField (auto_now = True , auto_now_add = False)
    proj_report = models.TextField()
    timestamp = models.DateTimeField (auto_now = True , auto_now_add = False , blank = True)

    def __str__ (self):
        return self.full_name