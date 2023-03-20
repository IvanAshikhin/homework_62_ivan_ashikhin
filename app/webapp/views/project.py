from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from webapp.models.project import Project
from webapp.models import Task
from webapp.forms import ProjectForm, AddProjectUserForm

from webapp.forms import ProjectTaskForm


class ProjectsIndexView(ListView):
    template_name = 'project_index.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetail(DetailView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        context['tasks'] = Task.objects.filter(project=project.pk).exclude(is_deleted=True)
        context['users'] = project.users.all()
        return context


class AddProjectView(CreateView):
    template_name = 'project_add.html'
    model = Project
    context_object_name = 'projects'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, *kwargs)


class ProjectTaskAddView(CreateView):
    template_name = 'add_task_project.html'
    model = Task
    form_class = ProjectTaskForm
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, *kwargs)

    def form_valid(self, form):
        project_id = self.kwargs.get('pk')
        task = form.save(commit=False)
        task.project_id = project_id
        task.save()
        return redirect('index_page')


class AddProjectUsers(CreateView):
    model = Project
    form_class = AddProjectUserForm
    success_url = reverse_lazy('index_projects')
    template_name = 'add_user_to_project.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.get_object()
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        user_id = self.request.POST.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        project = self.get_object()
        project.users.add(user)
        return redirect('project_detail', project.pk)


class DeleteProjectMember(DeleteView):
    model = Project
    success_url = reverse_lazy('index_projects')
    template_name = 'delete_project_member.html'

    def get_object(self):
        return get_object_or_404(Project, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.get_object()
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        user_id = self.request.POST.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        project = self.get_object()
        project.users.remove(user)
        return redirect('project_detail', project.pk)
