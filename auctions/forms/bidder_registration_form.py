from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()


class BidderRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        pass

    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]
