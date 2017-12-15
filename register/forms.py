from django.contrib.auth.models import User
from django import forms


class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # make user email field required
        self.fields['email'].required = True

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# class LoginForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

    # class Meta:
        # model = User
        # fields = ['username', 'password']
