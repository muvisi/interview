
# Create your models here.
from django.db import models
class RegisterForm1A(models.Model):
    firstname=models.CharField(max_length=50)
    secondname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    age=models.CharField(max_length=60)
    stream=models.CharField(max_length=30)
   
def __str__(self):
        return self.firstname