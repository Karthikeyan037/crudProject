from django.db import models

# Create your models here.
class employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.IntegerField()
    mail_add= models.CharField(max_length=100)