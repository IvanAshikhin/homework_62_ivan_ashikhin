from django.db import models

STATUS = (('new', 'новый'), ('in progress', 'в процессе'), ('done', 'выполнено'))


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Статус', null=False, choices=STATUS)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Status"
