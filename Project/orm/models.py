from django.db import models
from django.contrib.auth.models import User
import time
import os


class CityDistrict(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'city_district'
        ordering = ['id']


class Club(models.Model):
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=100, blank=True, null=True)
    since = models.CharField(max_length=100, blank=True, null=True)
    secretariat = models.TextField(blank=True, null=True)
    city_district = models.ForeignKey(CityDistrict, on_delete=models.CASCADE, related_name='clubs', blank=True, null=True)
    leader = models.CharField(max_length=100, blank=True, null=True)
    slogan = models.TextField(blank=True, null=True)
    # logo = models.ImageField(upload_to="club/logo",
    #                          null=True,
    #                          blank=True,
    #                          help_text="Upload Logo klub")
    
    def __str__(self):
        return self.name                         

    class Meta:
        db_table = 'club'
        ordering = ['register_number']

    



class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='members')

    name = models.CharField(max_length=50, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    born_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    draw_length = models.CharField(max_length=5, blank=True, null=True)
    position = models.CharField(max_length=25, blank=True, null=True)
    # picture = models.ImageField(upload_to=file_profile,
    #                         null=True,
    #                         blank=True,
    #                         help_text="Upload Potomu sebagai gambar profile",
    #                         default='user/avatar.png'
    #                         )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'member'