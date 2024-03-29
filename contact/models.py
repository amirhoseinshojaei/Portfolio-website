from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Contact (models.Model):

    name = models.CharField (max_length = 50)
    email = models.EmailField()
    phone = PhoneNumberField()
    message = models.TextField()
    