from django.forms import ModelForm, widgets, ModelMultipleChoiceField, CheckboxSelectMultiple
from tracker_app.models import Issue, Type

class IssueForm(ModelForm):
    issue_type = ModelMultipleChoiceField(
        queryset = Type.objects.all(),
        required = False,
        label='Тип'
        widget=CheckboxSelectMultiple()
    )
    class Meta:
        model = Issue
        fields = ['summary','description', 'status' ,'issue_type']
        widgets = {
            'summary': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание'
            }),
            'description': widgets.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Полное описание'
            }),
            'status': widgets.Select(attrs={
                'class': 'form-control',
            }),
        }
