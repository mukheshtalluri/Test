from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Record

class SignupForm(UserCreationForm):
    username = forms.CharField(label='', max_length=25, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username'}))
    first_name = forms.CharField(label='', max_length=25, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Firstname'}))
    last_name = forms.CharField(label='', max_length=25, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Lastname'}))
    email = forms.EmailField(label='', max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'}))
    password1 = forms.CharField(label='', max_length=25, widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Password'}))
    password2 = forms.CharField(label='', max_length=25, widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder' : 'First Name', 'class' : 'form-control'}))
    last_name = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder' : 'Last Name', 'class' : 'form-control'}))
    email = forms.CharField(label='', required=True, widget=forms.widgets.EmailInput(attrs={'placeholder' : 'Email', 'class' : 'form-control'}))
    phone = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder' : 'Phone no', 'class' : 'form-control'}))
    address = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder' : 'Address', 'class' : 'form-control'}))
    city = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder' : 'City', 'class' : 'form-control'}))
    state = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder' : 'State', 'class' : 'form-control'}))
    zipcode = forms.CharField(label='', required=True, widget=forms.widgets.TextInput(attrs={'placeholder' : 'Zipcode', 'class' : 'form-control'}))

    class Meta:
        model = Record
        exclude = ('user', )