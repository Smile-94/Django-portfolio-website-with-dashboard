from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Message(models.Model):
    sender_name=models.CharField(max_length=100,)
    sender_mail=models.EmailField(max_length=254)
    sender_message=models.TextField()
    send_date=models.DateField(auto_now=True,null=True,blank=True)
    send_time=models.TimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.sender_name+" "+str(self.sender_mail)

class Education(models.Model):
    pass_year=models.DateField(auto_now=False, auto_now_add=False)
    instituate=models.CharField(max_length=200)
    degree=models.CharField(max_length=200)

    def __str__(self):
        return self.degree
    
    def get_absolute_url(self):
        return reverse('admin_app:educations')

class Skills(models.Model):
    skill_caption=models.CharField(max_length=20)
    skill_des=models.CharField(max_length=100)

    def __str__(self):
        return self.skill_caption

    def get_absolute_url(self):
        return reverse('admin_app:skills')

class Expriences(models.Model):
    joning_date=models.DateField(auto_now=False, auto_now_add=False)
    leav_date=models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    designation=models.CharField(max_length=50)
    organization_name=models.CharField(max_length=100)

    def __str__(self):
        return self.designation+" "+self.organization_name
    
    def get_absolute_url(self):
        return reverse('admin_app:expriences')

