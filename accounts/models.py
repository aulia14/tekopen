from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    profesi = models.CharField(max_length=100,blank=True, null=True)
    no_telp = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=100,blank=True, null=True)
    temlahir = models.CharField(max_length=100, blank=True, null=True)    
    jadwal = models.CharField(max_length=100,blank=True, null=True)
    alamat =models.CharField(max_length=250,blank=True, null=True)

    about_me = models.TextField(blank=True, null=True)
    prevjob1 = models.CharField(max_length=100,blank=True, null=True)
    prevjobcorp1 = models.CharField(max_length=100, blank=True, null=True)
    prevjobdate1 = models.CharField(max_length=100, blank=True, null=True)
    prevjobdesc1 = models.TextField(blank=True, null=True)
    prevjob2 = models.CharField(max_length=100, blank=True, null=True)
    prevjobcorp2 = models.CharField(max_length=100, blank=True, null=True)
    prevjobdate2 = models.CharField(max_length=100, blank=True, null=True)
    prevjobdesc2 = models.TextField(blank=True, null=True)
    preveduc1 = models.CharField(max_length=150, blank=True, null=True)
    preveducuniv1 = models.CharField(max_length=150, blank=True, null=True)
    preveducdate1 = models.CharField(max_length=100, blank=True, null=True)
    preveducdesc1 = models.TextField(blank=True, null=True)
    preveduc2 = models.CharField(max_length=150, blank=True, null=True)
    preveducuniv2 = models.CharField(max_length=150, blank=True, null=True)
    preveducdate2 = models.CharField(max_length=100, blank=True, null=True)
    preveducdesc2 = models.TextField(blank=True, null=True)
    preveduc3 = models.CharField(max_length=150, blank=True, null=True)
    preveducuniv3 = models.CharField(max_length=150, blank=True, null=True)
    preveducdate3 = models.CharField(max_length=100, blank=True, null=True)
    preveducdesc3 = models.TextField(blank=True, null=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
