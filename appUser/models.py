from django.db import models
from django.contrib.auth.models import User


class Userinfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    password = models.CharField(("Şifre"), max_length=50)
    tel = models.CharField(("Telefon Numarası"), max_length=50)
    
    def __str__(self):
        return self.user.username
    

class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE) 
    name = models.CharField(("Profil Adı"), max_length=50)
    image = models.ImageField(("Profil Resmi"), upload_to='profil', max_length=200)
    password = models.CharField(("Profil Resmi"), max_length=50, default="0000")
    password_active = models.BooleanField(("Şifreyi Etkinleştir"), default=False)
    
    def __str__(self):
        return self.user.username
