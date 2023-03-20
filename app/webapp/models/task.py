from django.db import models
from webapp.models.status import Status
from webapp.models.type import Type
from webapp.models.project import Project


class Task(models.Model):
    summary = models.CharField(max_length=100, null=False, blank=True, verbose_name='Краткое описание')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    status = models.ForeignKey(Status, related_name='status', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ManyToManyField(to=Type, related_name='task_type',
                                  verbose_name='Тип задачи', blank=True)
    created_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Время создания')
    edit_time = models.DateTimeField(auto_now=False, null=True, verbose_name='Время редактирования')
    is_deleted = models.BooleanField(default=False)
    project = models.ForeignKey(Project, related_name='project', on_delete=models.PROTECT, verbose_name='Проект',
                                default=1)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f'{self.summary} - {self.description} - {self.status} - {self.type} - {self.created_at}'
