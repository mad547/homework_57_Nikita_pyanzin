from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.core.paginator import Paginator

from tracker_app.models import Project
from tracker_app.forms import ProjectForm, IssueInProjectForm


class ProjectListView(TemplateView):
    template_name = 'tracker_app/project_list.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('search', '')
        projects = Project.objects.all().order_by('-start_date')

        if search:
            projects = projects.filter(
                Q(name__icontains=search) | Q(description__icontains=search)
            )

        paginator = Paginator(projects, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['projects'] = page_obj
        context['search'] = search
        return context


class ProjectDetailView(TemplateView):
    template_name = 'tracker_app/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        context['project'] = project
        context['issues'] = project.issue_set.filter(is_deleted=False)
        return context


class ProjectCreateView(LoginRequiredMixin , CreateView):
    template_name = 'tracker_app/project_create.html'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        project = form.save()
        project.members.add(self.request.user)
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'tracker_app/project_update.html'
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'

def get_success_url(request):
    return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'tracker_app/project_confirm_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs) if False else super().get(request, *args, **kwargs)


class ProjectIssueCreateView(LoginRequiredMixin, FormView):
    template_name = 'tracker_app/issue_create.html'
    form_class = IssueInProjectForm

    def dispatch(self, request, *args, **kwargs):
        self.project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def form_valid(self, form):
        issue = form.save(commit=False)
        issue.project = self.project
        issue.save()
        form.save_m2m()
        return redirect('project_detail', pk=self.project.pk)