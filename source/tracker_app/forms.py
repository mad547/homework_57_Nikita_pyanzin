from cProfile import label

from django.core.exceptions import ValidationError
from django.forms import ModelForm, widgets, ModelMultipleChoiceField, CheckboxSelectMultiple
from tracker_app.models import Issue, Type

class IssueForm(ModelForm):
    issue_type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        required=False,
        label='Тип',
        widjet=CheckboxSelectMultiple()
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
            'issue_type': widgets.Select(attrs={
                'class': 'form-control',
            }),
        }

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 10:
            raise ValidationError('Краткое описание должно быть не короче 10 символов')
        return summary

    def clean(self):
        cleaned_data = super().clean()
        summary = self.cleaned_data.get('summary')
        description = self.cleaned_data.get('description')
        if summary and description and summary == description:
            raise ValidationError('краткое и полное описание не должны совпадать')
        return cleaned_data