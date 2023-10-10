from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=30)
    eligible=models.CharField(max_length=100)
    address=models.TextField()
    email=models.EmailField()
    phone=models.BigIntegerField()

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    eligible = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.BigIntegerField()

class BngJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=30)
    eligible = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.BigIntegerField()