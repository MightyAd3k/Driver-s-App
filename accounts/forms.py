from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


def pass_length_validation(value):
    if len(value) < 6:
        return ValidationError('Password is too short')


class CreateUserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), validators=[pass_length_validation])
    password1 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(), validators=[pass_length_validation])

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
        if data['password'] is not None and data['password'] != data['password1']:
            raise ValidationError('Passwords are different')
        return data
