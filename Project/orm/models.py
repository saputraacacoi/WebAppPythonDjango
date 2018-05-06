from django.db import models
from django.contrib.auth.models import User
import time
import os
from orm import FileUploader


class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'province'
        ordering = ['id']

class CityRegency(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cityregencys', blank=True, null=True)    
    name = models.CharField(max_length=100)
    adress = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    logo = models.ImageField(upload_to="cabang/logo",
                             null=True,
                             blank=True,
                             help_text="Upload Logo klub")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city_regency'
        ordering = ['id']


class Club(models.Model):
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100, blank=True, null=True)
    since = models.CharField(max_length=100, blank=True, null=True)
    secretariat = models.TextField(blank=True, null=True)
    cityregency = models.ForeignKey(CityRegency, on_delete=models.CASCADE, related_name='clubs', blank=True, null=True)
    leader = models.CharField(max_length=100, blank=True, null=True)
    slogan = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="club/logo",
                             null=True,
                             blank=True,
                             help_text="Upload Logo klub")
    def __str__(self):
        return self.name                         

    class Meta:
        db_table = 'club'
        ordering = ['register_number']

    
class Anggota(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='anggotas')
    name = models.CharField(max_length=50, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    born_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    draw_length = models.CharField(max_length=5, blank=True, null=True)
    position = models.CharField(max_length=25, blank=True, null=True)
    picture = models.ImageField(upload_to=FileUploader.file_profile,
                            null=True,
                            blank=True,
                            help_text="Upload Potomu sebagai gambar profile",
                            default='user/avatar.png'
                            )
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'anggota'
        ordering = ['id']


class ClubFiles(models.Model):
    uploaded = models.DateTimeField(auto_now=True, auto_now_add=False)
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name='clubfiles')
    file = models.FileField(upload_to=FileUploader.file_club)
    filename = models.CharField(max_length=30, default=None)
    file_ext = models.CharField(max_length=30, default=None)
    mimetype = models.CharField(max_length=30, default=None)

    class Meta:
        db_table = 'club_files'

    def __str__(self):
        return self.file.name

class CabangFiles(models.Model):
    uploaded = models.DateTimeField(auto_now=True, auto_now_add=False)
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name='cabangfiles')
    file = models.FileField(upload_to=FileUploader.file_club)
    filename = models.CharField(max_length=30, default=None)
    file_ext = models.CharField(max_length=30, default=None)
    mimetype = models.CharField(max_length=30, default=None)

    class Meta:
        db_table = 'cabang_files'

    def __str__(self):
        return self.file.name

class PenCab(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class PenClub(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class TestGrafik(models.Model):
    nama = models.CharField(max_length=50, blank=True, null=True) 
    gender =  models.CharField(max_length=50, blank=True, null=True)   
    usia =  models.CharField(max_length=50, blank=True, null=True)   
    k_busur =  models.CharField(max_length=50, blank=True, null=True) 





  
    
    
    
