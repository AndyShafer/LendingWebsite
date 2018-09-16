from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        #fields = ['firstName', 'lastName', 'username', 'email', 'phone', 'address', 'city', 'state', 'password']
        fields = ['username', 'email', 'password']
