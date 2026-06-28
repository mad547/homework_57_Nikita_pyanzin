from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView

from tracker_app.models import Issue
from tracker_app.forms import IssueForm


class IssueListView(TemplateView):
    template_name = 'tracker_app/issue_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.filter(is_deleted=False)
        return context


class IssueDetailView(DetailView):
    template_name = 'tracker_app/issue_detail.html'
    context_object_name = 'issue'

    def get_queryset(self):
        return Issue.objects.filter(is_deleted=False)


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'tracker_app/issue_update.html'
    form_class = IssueForm
    context_object_name = 'issue'

    def get_queryset(self):
        return Issue.objects.filter(is_deleted=False)

    def test_func(self):
        issue = self.get_object()
        user = self.request.user
        in_project = issue.project.members.filter(pk=user.pk).exists()
        return in_project and user.has_perm('tracker_app.change_issue')

    def form_valid(self, form):
        issue = form.save(commit=False)
        issue.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('issue_detail', kwargs={'pk': self.object.pk})


class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'tracker_app/issue_delete.html'
    context_object_name = 'issue'
    success_url = reverse_lazy('project_list')

    def get_queryset(self):
        return Issue.objects.filter(is_deleted=False)

    def test_func(self):
        issue = self.get_object()
        user = self.request.user
        in_project = issue.project.members.filter(pk=user.pk).exists()
        return in_project and user.has_perm('tracker_app.delete_issue')

    def form_valid(self, form):
        issue = self.get_object()
        issue.is_deleted = True
        issue.save()
        return super(DeleteView, self).form_valid(form)