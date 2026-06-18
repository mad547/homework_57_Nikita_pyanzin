from django.core.exceptions import ValidationError
from django.forms import ModelForm, widgets, ModelMultipleChoiceField, CheckboxSelectMultiple
from tracker_app.models import Issue, Type, Project

class IssueForm(ModelForm):
    issue_type = ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        required=False,
        label='Тип',
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


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name','description', 'start_date' ,'end_date']
        widgets = {
            'name': widgets.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название проекта'
            }),
            'description': widgets.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Описание проекта'
            }),
            'start_date': widgets.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'end_date': widgets.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            })
        }


class IssueInProjectForm(ModelForm):
    issue_type = ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        required=False,
        label='Тип',
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

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 10:
            raise  ValidationError('Краткое описание должно быть не короче 10 символов')
        return summary