# from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
# from django.contrib.auth import get_user_model
# User = get_user_model()
from auctions.models import Auctioneer


class AuctioneerRegistration(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Auctioneer
        fields = ['name', ]
