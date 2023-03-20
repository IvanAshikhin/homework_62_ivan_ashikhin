from django.db import models


TYPE = (('task', 'задача'), ('bug', 'ошибка'), ('enhancement', 'улучшение'))


class Type(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Тип задачи', choices=TYPE)

    def __str__(self):
        return self.name



