from django import forms
from django.core.validators import BaseValidator

from .models import Task
from .models.project import Project


class MaxLengthValidator(BaseValidator):
    def __init__(self, limit_value=100):
        message = ('Максимальная длинна не может быть больше %(limit_value)s знаков.')
        super().__init__(limit_value=limit_value, message=message)

    def compare(self, value, limit_value):
        return limit_value <= len(value)


class TaskForm(forms.ModelForm):
    summary = forms.CharField(validators=[MaxLengthValidator()])
    description = forms.CharField()

    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'status', 'project']
        labels = {
            'summary': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип задачи',
            'project': 'Проект'

        }


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()

        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
        }


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'type', 'status']
        labels = {
            'summary': 'Заголовок',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип задачи'
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Find')
