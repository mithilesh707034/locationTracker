from django.db import models

class Member(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='',null=True,blank=True)
    email=models.EmailField(default='',null=True,blank=True)
    phone=models.CharField(max_length=10,default='',null=True,blank=True)
    latitude=models.TextField(default='',null=True,blank=True)
    longitude=models.TextField(default='',null=True,blank=True)
    def __str__(self):
        return (self.name)
