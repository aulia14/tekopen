from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo','profesi','no_telp','status','temlahir',
        'jadwal','alamat','about_me','prevjob1','prevjobcorp1','prevjobdate1', 'prevjobdesc1',
        'prevjob2','prevjobcorp2','prevjobdate2', 'prevjobdesc2',
        'preveduc1','preveducuniv1','preveducdate1', 'preveducdesc1',
        'preveduc2','preveducuniv2','preveducdate2', 'preveducdesc2',
        'preveduc3','preveducuniv3','preveducdate3', 'preveducdesc3',
        )
