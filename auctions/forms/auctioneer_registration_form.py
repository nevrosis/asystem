# from django.contrib.auth.models import User
from django import forms
# from django.contrib.auth import get_user_model
# User = get_user_model()
from auctions.models import Auctioneer


class AuctioneerRegistration(forms.ModelForm):

    class Meta:
        model = Auctioneer
        fields = ['name', ]
