from django.db import models

# Create your models here.
class admin_log(models.Model):
    email = models.EmailField()
    psw = models.CharField(max_length=25)