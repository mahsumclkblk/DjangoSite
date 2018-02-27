from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    title=models.CharField(verbose_name="Ad",max_length=123,default="Başlık")
    image1=models.ImageField(verbose_name="Profil",blank=True,null=True)

    who=models.TextField(max_length=500,verbose_name="Hakkımda",blank=True,default="Kim")
    what_to_do=models.TextField(max_length=500,verbose_name="Ne Yaparım ?",blank=True,default="Ne yapar")

    interested_1=models.TextField(max_length=500,verbose_name="İlgi Alanlarım 1",blank=True,default="İlgi Alanı")
    img1=models.ImageField(verbose_name="İmg 1",blank=True)
    interested_2=models.TextField(max_length=500,verbose_name="İlgi Alanlarım 2",blank=True,default="İlgi Alanı")
    img2 = models.ImageField(verbose_name="İmg 2",blank=True)

    interested_3=models.TextField(max_length=500,verbose_name="İlgi Alanlarım 3",blank=True,default="İlgi Alanı")
    img3 = models.ImageField(verbose_name="İmg 3",blank=True)

    def __str__(self):
        return "{} - {} ".format(self.title,self.id)
