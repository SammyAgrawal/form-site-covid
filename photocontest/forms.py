from django import forms
from .models import Profile, Submission

class Submit(forms.ModelForm):
    class Meta:
        model=Submission
        fields=['author', 'photo', 'caption']
        