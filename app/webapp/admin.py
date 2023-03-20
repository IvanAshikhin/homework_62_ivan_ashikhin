from django.contrib import admin

from webapp.models import Task
from webapp.models import Status
from webapp.models import Type


# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    fields = ('name',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    fields = ('name',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status', 'created_at', 'edit_time')
    list_filter = ('id', 'summary', 'description', 'status', 'type', 'created_at', 'edit_time')
    search_fields = ('id', 'summary', 'description', 'status', 'type')
    fields = ('id', 'summary', 'description', 'status', 'type', 'created_at', 'edit_time')
    readonly_fields = ('id', 'created_at', 'edit_time')


admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
