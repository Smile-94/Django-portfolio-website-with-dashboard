from django.forms import ModelForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from django.contrib.auth.forms import UserCreationForm

#import models
from login_app.models import User
from login_app.models import Profile

class ProfileForm(ModelForm):
    phone_number=PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='BD')
    )

    class Meta:
        model = Profile
        exclude = ("user",)

