from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import re


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


def pass_length_validation(value):
    if len(value) < 8:
        raise ValidationError('Password is too short')


def pass_lower_case_validation(value):
    if re.search('[a-z]', value) is None:
        raise ValidationError('Password must contains at least one lowercase character')


def pass_upper_case_validation(value):
    if re.search('[A-Z]', value) is None:
        raise ValidationError('Password must contains at least one uppercase character')


def pass_number_validation(value):
    if re.search('[0-9]', value) is None:
        raise ValidationError('Password must contains at least one number')


def pass_special_sign_validation(value):
    if re.search('[^A-Za-z0-9]', value) is None:
        raise ValidationError('Password must contains at least one special symbol')


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               help_text=('Required at least: one big letter, small letter, number '
                                          'and one special sign: ! @ # $ % ^ & * ( ) ? - _ /'),
                               widget=forms.PasswordInput(),
                               validators=[pass_length_validation,
                                           pass_special_sign_validation,
                                           pass_lower_case_validation,
                                           pass_upper_case_validation,
                                           pass_number_validation])

    password1 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput(),
                                validators=[pass_length_validation])

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'password1'
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        verifier = User.objects.filter(username=username)
        if verifier.exists():
            raise ValidationError('User already exists')
        return username

    def clean(self):
        data = super().clean()
        if data.get('password') is not None and data.get('password') != data.get('password1'):
            raise ValidationError('Passwords are different')
        return data
