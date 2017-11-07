from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils import encoding


ADM = "ADMIN"
MAN = "MANAGER"
    
ROLES = (
    (ADM, "ADMIN"),
    (MAN, "MANAGER"),
)

class User(AbstractUser):    
# Create your models here.
    #REQUIRED_FIELDS = ('username',)  
    username = models.CharField(unique=True,max_length = 20)
    password = models.CharField(max_length = 16)
    list_of_roles = models.CharField(max_length= 9,choices = ROLES,default = MAN)
    #USERNAME_FIELD = 'username'
    
   
@python_2_unicode_compatible
class Company(models.Model):

    name = models.CharField(unique=True,max_length=30)
    tel = PhoneNumberField()
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.name

