
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

GENDER_CHOICES = (
    ('E', 'Erkek'),
    ('K', 'Kadın'),
)



class Person(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    tcno = models.CharField(max_length=11, blank=True, null=True, default=None)
    name_surname = models.CharField(
        max_length=50, blank=True, null=True, default=None)
    gender = models.CharField(max_length=128, choices=GENDER_CHOICES,
                              blank=True, null=True)
    birth_date = models.CharField(max_length=12, blank=True, null=True)
    job = models.CharField(max_length=30, null=True, blank=True)
    birth_city = models.CharField(max_length=20, blank=True, null=True)
    father = models.CharField(max_length=40, blank=True, null=True)
    mother = models.CharField(max_length=40, blank=True, null=True)
    son = models.CharField(max_length=40, blank=True, null=True)
    daughter = models.CharField(max_length=40, blank=True, null=True)
    living_city = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    create_time = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.name_surname





class Contact(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    fullname=models.CharField(max_length=30,null=False,blank=False,default="İsimsiz Kullanıcı")
    phone = models.TextField(max_length=11,null=False,blank=False,default="Yok")
    email = models.EmailField(null=False, blank=False)
    desc = models.TextField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.email



class Responser(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    resp = models.TextField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    
    def __str__(self):
        return self.resp



class Announcement(models.Model):
    
    title=models.CharField(max_length=30,blank=False,null=False)
    desc=models.TextField(max_length=200,blank=False,null=False)
    # image=models.ImageField(null=True,blank=True,upload_to="duyuru")
    create_time = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.title


class IstekOneri(models.Model):
    adsoyad = models.CharField(max_length=30,blank=False,null=False)
    acıklama=models.TextField(max_length=300,blank=False,null=False)
    numara = models.CharField(max_length=11,blank=True,null=True)
    image=models.ImageField(null=True,blank=True,upload_to="istekoneri")
    create_time = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    update_time = models.DateTimeField(auto_now=True,blank=True, null=True) 

    def __str__(self):
        return self.adsoyad

# Create your models here.
