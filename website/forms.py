from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from website.models import Record

class SignupForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}), label='')
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}), label='')
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}), label='')
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Phone', 'class':'form-control'}), label='')
    city = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'City', 'class':'form-control'}), label='')
    state = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'State', 'class':'form-control'}), label='')
    zipcode = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Zip Code', 'class':'form-control'}), label='')
    
    class Meta:
        model = Record
        exclude = ('user',)
        