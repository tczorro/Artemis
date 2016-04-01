from django import forms
from myhorton.models import HT

class HortonForm(forms.ModelForm):
    basis = forms.CharField()
    alpha = forms.CharField()
    beta = forms.CharField()
    scf = forms.CharField()
    class Meta:
        model = HT
        fields = (
            'molecule', 
                )
