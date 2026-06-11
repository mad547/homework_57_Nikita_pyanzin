from django.forms import ModelForm, widgets
from tracker_app.models import Issue

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ['summary','description', 'status' ,'issue_type']
        widgets = {
            'summary': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание'
            }),
            'descriptions': widgets.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Полное описание'
            }),
            'status': widgets.Select(attrs={
                'class': 'form-control',
            }),
            'issue_type': widgets.Select(attrs={
                'class': 'form-control',
            }),
        }
