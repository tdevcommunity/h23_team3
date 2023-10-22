from django import forms
from .models import Users


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

    is_mentor = forms.BooleanField(label='Mentor', required=False)
    is_mentore = forms.BooleanField(label='Mentore', required=False)