from . import views
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


class choreForm (forms.ModelForm):

    class Meta:
        model = chores
        fields = ['name', 'points', 'character']
    def __init__(self, *args, **kwargs):
        super(choreForm, self).__init__(*args, **kwargs)
        self.fields['character'].queryset = character.objects.filter(level=1)

class userForm (UserCreationForm):
    username = forms.CharField(label='username', min_length=5, max_length=150)  
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['password1']  
        )
        return user    
    
