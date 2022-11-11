
from django.db import models
from django.urls import reverse

#To create phone number field in django model
from phonenumber_field.modelfields import PhoneNumberField

#To create a custom user model and admin panel
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy

#To create automatically create one to one objects
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class MyUserManager(BaseUserManager):

    """A custom manager to deal with emails and custom identifiers"""

    def _create_user(self,email,password, **extra_fields):
        """Create and saves a user with a given email and password"""

        if not email:
            raise ValueError('The email must be set!')
        
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("usperuser must have is_staff=True")
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        return self._create_user(email,password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email=models.EmailField(unique=True,null=False)
    is_staff=models.BooleanField(
        gettext_lazy('staff_status'),default=False,
        help_text=gettext_lazy('designets wheter the user can loin to this site'),
    )

    is_active=models.BooleanField(
        gettext_lazy('active'),default=True,
        help_text=gettext_lazy('designets wheter the user can loin to this site'),
    )

    USERNAME_FIELD='email'

    objects=MyUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    fullName=models.CharField(max_length=264,blank=True)
    address_home=models.CharField(max_length=200,blank=True,null=True)
    address_office=models.CharField(max_length=200,blank=True,null=True)
    phone_number=PhoneNumberField(blank=True,null=True)
    profile_pic=models.ImageField(upload_to='profile_pic',default='defoult.jpg')

    
    def __str__(self):
        return self.fullName+"'s profile"

    def fully_filled(self):
        fields_name=[f.name for f in self._meta.get_fields()]

        for field_name in fields_name:
            value=getattr(self,field_name)

            if value is None or value=='':
                return False

        return True
    
    def get_absolute_url(self):
        return reverse('admin_app:profile')

@receiver(post_save,sender=User)

def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()