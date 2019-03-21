from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:                                                   # give us nested namespace for configurations
                                                                  # and keeps them in one place
        model = User
        fields = ['username', 'email', 'password1', 'password2']
