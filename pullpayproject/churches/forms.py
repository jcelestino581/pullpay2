from django import forms
from .models import Church, Users


class ChurchForm(forms.ModelForm):
    class Meta:
        model = Church
        fields = ["church_name_text", "size_int", "church_type_text"]
        widgets = {
            "church_type_text": forms.Select(),  # Renders as a dropdown
        }


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users  # Specify the model to create the form from
        fields = [
            "user_first_name",
            "user_last_name",
            "email",
            "phone_number",
            "address",
            "payment_method",
            "churches",  # Include churches field for many-to-many relationship
        ]
        widgets = {
            "churches": forms.CheckboxSelectMultiple()  # Render as checkboxes for multiple selection
        }
