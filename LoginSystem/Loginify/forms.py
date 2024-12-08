from django import forms
from .models import UserDetail

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput(),label="Password")

