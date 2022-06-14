
from platform import python_version
from types import CoroutineType
from unicodedata import name
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    phoneno=models.CharField(max_length=12)
    city=models.CharField(max_length=10)
    pin=models.CharField(max_length=6)

    def __str__(self):
         return self.name