from django import forms
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegistraionForm(forms.Form):
    username = forms.CharField(widget =forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget =forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Create Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # confirm_password = forms.CharField(label='Confirm Passwordd', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already exists')
        return email
    
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     username = User.objects.filter(username=username).exists()
    #     if username:
    #         raise ValidationError('this username already exists')
    #     return username
    
class UserLoginForm(forms.Form):
    username = forms.CharField(label='', widget =forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))