from django.db import models

# Create your models here.
class shop_log(models.Model):
    email = models.EmailField()
    pasw = models.CharField(max_length=25)
   
class newstock(models.Model):
    mnm = models.CharField(max_length=25)
    mpr = models.IntegerField()
    mim = models.FileField(upload_to='pictures')
    cat = models.CharField(max_length=25)
    bran = models.CharField(max_length=25)
    des = models.TextField()
    dis = models.CharField(max_length=25)
    mfg = models.DateField()
    exp = models.DateField()
    
    
