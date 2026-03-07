from django import forms

from .models import Company

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    # Custom validation for the name field
    # the <fieldname> method is used to add custom validation to a field.
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            # this will raise an validation error if the name is less than 2 characters long.
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name

    # Custom validation for the message field
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message
    
    class CompanyForm(forms.ModelForm):
    # the inner Meta class tells django which model to use and which fields to include in the form
      class Meta:
        model = Company
        fields = ['name', 'email', 'website']
        # note in our model we also have created_at and updated_at fields, but we don't need to include them in the form since they are automatically set by django