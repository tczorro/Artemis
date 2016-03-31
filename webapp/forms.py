from django import forms
from webapp.models import TS

class SaddleForm(forms.ModelForm):
    class Meta:
        model = TS
        fields = ("ratio", "auto_ic", "reactant", "product")
