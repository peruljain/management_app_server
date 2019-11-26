from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Database(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    visitor_name=models.CharField(max_length=100,default='')
    visitor_email=models.CharField(max_length=100,default='')
    visitor_phone=models.CharField(max_length=100,default='')
    host_name=models.CharField(max_length=100,default='')
    host_email=models.CharField(max_length=100,default='')
    host_phone=models.CharField(max_length=100,default='')
    time = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
         database=Database.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)