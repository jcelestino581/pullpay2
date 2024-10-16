from django import forms
from .models import Church, User, Transaction

# from churches.models import User


class ChurchForm(forms.ModelForm):
    class Meta:
        model = Church
        fields = ["church_name_text", "size_int", "church_type_text"]
        widgets = {
            "church_type_text": forms.Select(),  # Renders as a dropdown
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount"]  # Only include 'amount' in the form

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)  # Extract the user from kwargs
        super(TransactionForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        transaction = super(TransactionForm, self).save(commit=False)
        # Set the userKey to the current user
        transaction.userKey = self.user  # Assign the userKey here
        if commit:
            transaction.save()
        return transaction


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            "user_first_name",
            "user_last_name",
            "email",
            "phone_number",
            "address",
            "payment_method",
            "password",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password
        if commit:
            user.save()
        return user
