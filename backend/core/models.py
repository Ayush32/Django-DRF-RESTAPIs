from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,null= False)
    last_name = models.CharField(max_length=100,null = False)
    company_name = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    zip = models.IntegerField(null = False)
    email = models.EmailField(null = False)
    web = models.URLField(max_length=200)
    age = models.IntegerField()



