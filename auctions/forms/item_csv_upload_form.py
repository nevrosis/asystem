from django import forms


class ItemCSVUploadForm(forms.Form):
    csv_file = forms.FileField()
