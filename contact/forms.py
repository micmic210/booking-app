from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for handling contact submissions.
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'autocomplete': 'off',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email',
                'autocomplete': 'off',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Message',
                'autocomplete': 'off',
            }),
        }

    def clean_name(self):
        """
        Validates the 'name' field.
        """
        name = self.cleaned_data.get("name", "").strip()
        if not name:
            raise forms.ValidationError("Please enter your name.")
        return name

    def clean_email(self):
        """
        Validates the 'email' field.
        """
        email = self.cleaned_data.get("email", "").strip()
        if not email:
            raise forms.ValidationError("Please enter your email.")
        return email

    def clean_message(self):
        """
        Validates the 'message' field.
        """
        message = self.cleaned_data.get("message", "").strip()
        if not message:
            raise forms.ValidationError("Please enter your message.")
        return message
