from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, render
from django.views import View

from tracker_app.models import Project
from tracker_app.views.mixins import ProjectMemberMixin


class ProjectMembersView(LoginRequiredMixin, ProjectMemberMixin, View):
    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))

    def get(self, request, pk):
        project = self.get_project()
        users = get_user_model().objects.exclude(pk__in=project.members.all())
        return render(request, 'tracker_app/project_members.html', {
            'project': project,
            'users': users,
        })


class ProjectMemberAddView(LoginRequiredMixin, ProjectMemberMixin, View):
    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))

    def post(self, request, pk):
        project = self.get_project()
        user_pk = request.POST.get('user_pk')
        user = get_object_or_404(get_user_model(), pk=user_pk)
        project.members.add(user)
        return redirect('project_members', pk=project.pk)


class ProjectMemberRemoveView(LoginRequiredMixin, ProjectMemberMixin, View):
    def get_project(self):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))

    def post(self, request, pk, user_pk):
        project = self.get_project()
        user = get_object_or_404(get_user_model(), pk=user_pk)
        project.members.remove(user)
        return redirect('project_members', pk=project.pk)