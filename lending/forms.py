from django.contrib.auth.models import User
from .models import Profile, Object
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'city', 'state', 'bio']
        
class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ['name', 'description']
