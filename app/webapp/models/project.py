from django.db import models


class Project(models.Model):
    start_date = models.DateField(auto_now=False, null=False, verbose_name='Дата начала')
    end_date = models.DateField(auto_now=False, null=True, verbose_name='Дата окончания')
    name = models.CharField(max_length=100, null=False, blank=True, verbose_name='Название')
    description = models.TextField(max_length=1000, null=False, verbose_name='Описание')

    def __str__(self):
        return f' {self.name} - {self.description} {self.start_date} {self.end_date} '

