from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    # email = models.TextField(max_length=255,unique=True)
    # created_on = models.DateTimeField(auto_now_add=True)



