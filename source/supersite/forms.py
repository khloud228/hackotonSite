from django import forms
from django.contrib.auth.models import User

from .models import Video, Camera


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video',)


class CameraAddForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ('camera_url', 'username', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пожалуйста убедитесь, что во второй раз вы ввели пароль верно.')
        return cd['password2']
    
    def clean_email(self):
        return str(self.cleaned_data['email'][0]).lower() + self.cleaned_data['email'][1:]
