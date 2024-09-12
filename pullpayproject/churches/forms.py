from django import forms
from .models import Church

class ChurchForm(forms.ModelForm):
    class Meta:
        model = Church
        fields = ['church_name_text', 'size_int', 'church_type_text']
        widgets = {
            'church_type_text': forms.Select(),  # Renders as a dropdown
        }