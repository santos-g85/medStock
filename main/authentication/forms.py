from django import forms

class SignUPForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    email = forms.EmailField(label="email")