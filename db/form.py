from django import forms

class SubscribeForm(forms.Form):
  name = forms.CharField(label='Your Name', max_length=100)
  phone_number = forms.CharField(label='Phone Number', max_length=12, min_length=10)