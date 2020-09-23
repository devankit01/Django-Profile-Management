from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PMS(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50,unique = True)
	phone = models.CharField(max_length=15,unique = True)
	occupation = models.CharField(max_length=50)
	profile = models.CharField(max_length=60)
	username = models.OneToOneField(User,on_delete = models.CASCADE)

