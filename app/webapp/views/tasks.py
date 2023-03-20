from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Task
from webapp.forms import TaskForm


class TaskDetail(DetailView):
    template_name = 'task.html'
    model = Task
    context_object_name = 'tasks'


class TaskUpdateView(UpdateView):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'tasks'

    def get_success_url(self):
        return reverse('detail_task', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, *kwargs)


class TaskDeleteView(DeleteView):
    template_name = 'delete.html'
    context_object_name = 'tasks'
    model = Task
    success_url = reverse_lazy('index_page')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, *kwargs)


class TaskAddView(CreateView):
    template_name = 'task_add.html'
    model = Task
    context_object_name = 'tasks'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('detail_task', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, *kwargs)
