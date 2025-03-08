from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class buyForm(forms.ModelForm):
    class Meta:
        model = buy
        fields = '__all__'

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'

class sellForm(forms.ModelForm):
    class Meta:
        model = sell
        fields = ['housename', 'price', 'bedrooms', 'bathrooms', 'location', 
                  'square_feet', 'description', 'house_type', 'image', 
                  'outside_image', 'livingroom_image', 'bedroom_image', 
                  'kitchen_image', 'bathroom_image', 'additional_image1', 
                  'additional_image2', 'property_history', 'built_year']




class PropertyUsageForm(forms.ModelForm):
    class Meta:
        model = PropertyUsage
        fields = ['user', 'starting_year', 'ending_year', 'price']


class SiginForm(forms.ModelForm):
    class Meta:
        model = sigin
        fields = ['username', 'email', 'phone', 'password']

    def save(self):
        obj = super().save()
        obj.set_password(self.cleaned_data['password'])
        obj.save() 
        print('hi') 
        return obj

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class loginForm(AuthenticationForm):
    # Customize the form if needed
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


# forms.py
from django import forms

class SearchForm(forms.Form):
    location = forms.CharField(max_length=100, required=True, label='Location')


# forms.py (add new form)
from .models import AgentInquiry

class AgentInquiryForm(forms.ModelForm):
    class Meta:
        model = AgentInquiry
        fields = ['name', 'mobile', 'email', 'message']