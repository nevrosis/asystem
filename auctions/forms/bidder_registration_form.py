from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth import get_user_model
User = get_user_model()


class BidderRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    def clean(self):
        pass

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]
