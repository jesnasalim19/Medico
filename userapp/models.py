from django.db import models
from ShopOwner.models import newstock
# Create your models here.
class reg_tbl(models.Model):
    fnm = models.CharField(max_length=25)
    mob = models.IntegerField()
    eml = models.EmailField()
    psw1 = models.CharField(max_length=25)
    psw2 = models.CharField(max_length=25)

class Cart_tbl(models.Model):
    customer = models.ForeignKey(reg_tbl,on_delete=models.CASCADE)
    product = models.ForeignKey(newstock,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

class Pay_tbl(models.Model):
    pro = models.CharField(max_length=25)
    qty = models.IntegerField()
    prc = models.IntegerField()
    tot = models.IntegerField()
    fn = models.CharField(max_length=25)
    cd = models.IntegerField()
    ex = models.DateField()
    cvv = models.CharField(max_length=25)
    
class feed_tbl(models.Model):
    fnm = models.CharField(max_length=25)
    eml = models.EmailField()
    feed = models.TextField()