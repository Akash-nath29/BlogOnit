from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'class': 'form-control border-3'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control border-3'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control border-3'}))

    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control border-3'
        self.fields['password1'].widget.attrs['class'] = 'form-control border-3'
        self.fields['password2'].widget.attrs['class'] = 'form-control border-3'
        
        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.', widget=forms.EmailInput(attrs={'class': 'form-control border-3'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control border-3'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control border-3'}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control border-3'}))
    # last_login = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control border-3'}))
    # is_superuser = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check border-3'}))
    # is_staff = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check border-3'}))
    # is_active = forms.CharField(max_length=255, widget=forms.CheckboxInput(attrs={'class': 'form-check border-3'}))
    # date_joined = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control border-3'}))

    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
