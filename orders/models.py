from distutils.command.upload import upload
from django.db import models

# Create your models here.


class jobs(models.Model): 
    list_jobs = models.CharField(max_length=200)
    def __str__(self): 
        return self.list_jobs

class Data(models.Model): 
    id_data = models.AutoField(primary_key=True)
    in_date = models.DateField()
    name_customer = models.CharField(max_length=200)
    jobs = models.ForeignKey(jobs, on_delete=models.CASCADE)
    out_date = models.DateField()
    upload = models.URLField(blank=True)
    def __str__(self): 
        return self.name_customer

class Status(models.Model):
    id_status = models.ForeignKey(Data, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    def __str__(self): 
        return self.status
