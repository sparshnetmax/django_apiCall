from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    refreshToken = models.CharField(max_length=255,null=True,default=None,blank=True)
    # email = models.TextField(max_length=255,unique=True)
    # created_on = models.DateTimeField(auto_now_add=True)



