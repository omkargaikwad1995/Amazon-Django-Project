from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _


class CustomerRegistrationForm(UserCreationForm):
    password1: forms.CharField(label='Password', widget=forms.PasswordInput
    (attrs={'class':'form-control'}))
    password1: forms.CharField(label='Confirm Password again', widget=forms.PasswordInput
    (attrs={'class':'form-control'}))
    email=forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        labels={'email':'Email'}
        Widgets={'username':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput
    (attrs={'autocomplete':'current-password','class':'form-control'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_('Old Password'),strip=False, widget=forms.PasswordInput
    (attrs={'autocomplete':'current-password', 'autofocus':True, 'class':'form-control'}))
    
    new_password1=forms.CharField(label=_('New Password'),strip=False, widget=forms.PasswordInput
    (attrs={'autocomplete':'new-password', 'autofocus':True, 'class':'form-control'}))
    
    new_password2=forms.CharField(label=_('Confirm New Password'),strip=False, widget=forms.PasswordInput
    (attrs={'autocomplete':'new-password', 'autofocus':True, 'class':'form-control'}))