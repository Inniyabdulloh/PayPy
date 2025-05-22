from . import models
from django import forms



class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ['username', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # parolni hashlash
        if commit:
            user.save()
        return user


class CreateTokenForm(forms.ModelForm):
    class Meta:
        model = models.Token
        fields = ['name']