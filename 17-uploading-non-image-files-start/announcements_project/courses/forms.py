from django import forms

class BulkAssignmentUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')

    # Validation
    def clean_csv_file(self):
        file = self.cleaned_data.get('csv_file')
        # Check #1: Validate the file type extension
        if file and not file.name.endswith('.csv'):
           raise forms.ValidationError('Only CSV files are allowed.')
        
        # Check #2: Does the browser report it as text/csv?
        if file and file.content_type != 'text/csv':
            raise forms.ValidationError("File type is not CSV.")

        # if no errors are raised we return the file 
        return file
   