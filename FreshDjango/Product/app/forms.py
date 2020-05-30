from django import forms
from django.core import validators
from .models import RegisterUser, UserProfileInfo
from django.contrib.auth.models import User

# Define your forms here.

class RegForm(forms.ModelForm):

    hashedPassword = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirmedPassword = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        clean_data = super().clean()

        cleanHashedPassword = clean_data['hashedPassword']
        cleanConfirmedPassword = clean_data['confirmedPassword']
        
        if cleanHashedPassword != cleanConfirmedPassword:
            raise forms.ValidationError("Password doesn't matches to each other")
        
    class Meta():
        model = RegisterUser

        exclude = ('confirmedPassword',)

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model = User

        fields = ('username', 'email', 'password',)

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo

        fields = ('portfolio', 'picture',)
