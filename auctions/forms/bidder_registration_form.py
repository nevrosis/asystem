from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from django.contrib.auth import get_user_model
User = get_user_model()


class BidderRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', ]
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if "xxx" in first_name:
            raise forms.ValidationError("no valid Fist name")
        return first_name

