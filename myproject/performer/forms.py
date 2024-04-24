from django import forms

from performer.models import PerformerProfile


class PerformerProfileForm(forms.ModelForm):
    class Meta:
        model = PerformerProfile
        fields = ['contact_info', 'experience']
