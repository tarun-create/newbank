from django.db import models

# Create your models here.
class account_view(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    acc = models.CharField(max_length=250)
    ifsc = models.CharField(max_length=20)
    branch = models.CharField(max_length=120)

class salary_view(models.Model):
    acc = models.CharField(max_length=250)
    branch = models.CharField(max_length=120)
    