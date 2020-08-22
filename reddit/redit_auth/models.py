from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    Appuser = models.CharField(max_length=255,unique=True)
    refreshToken = models.CharField(max_length=255,null=True,default=None,blank=True)



