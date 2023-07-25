from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from store import models



# Create your forms here.

class SignupForm(UserCreationForm):
    username = forms.CharField(label="Username:", max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label="Password:", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Confirm Password:", widget=forms.PasswordInput)

    def username_clean(self):
        username = self.cleaned_data['username']
        new = User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError('user already exists')
        return username

    def clean_password(self):
        pass1 = self.cleaned_data['password1']
        pass2 = self.cleaned_data['password2']
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('pass not match')
        return pass2

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput)


class contactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50, required=True)
    email = forms.CharField(label="Email", max_length=20, required=True)
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={'rows': 6, 'cols': 25}), required=True)
