from django.contrib.auth.models import User
from django.contrib.admin import widgets
from bootstrap_datepicker_plus import DatePickerInput
from datetimewidget.widgets import DateWidget
from .models import Profile, Object, Contract
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

class RequestForm(forms.ModelForm):
    #date = forms.DateField(widget=DatePickerInput(options={"format": "mm/dd/yyyy", "autoclose": True}))
    class Meta:
        model = Contract
        fields = ['startTime', 'endTime']

'''
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['startTime'].widget = widgets.AdminSplitDateTime()
        self.fields['endTime'].widget = widgets.AdminSplitDateTime()
'''

