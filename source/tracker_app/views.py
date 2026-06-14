from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, FormView


from tracker_app.models import Issue
from tracker_app.forms import IssueForm


# Create your views here.
class IssueListView(TemplateView):
    template_name = 'tracker_app/issue_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueDetailView(TemplateView):
    template_name = 'tracker_app/issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super.get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        return context


class IssueCreateView(FormView):
    template_name = 'tracker_app/issue_create.html'
    form_class = IssueForm
    success_url = reverse_lazy('issue_list')

    def form_valid(self, form):
        types = form.cleaned_data.pop('issue_type')
        issue = form.save()
        issue.issue_type.set(types)
        return super().form_valid(form)


class IssueUpdateView(FormView):
    template_name = 'tracker_app/issue_update.html'
    form_class = IssueForm

    def dispatch(self, request, *args, **kwargs):
        self.issue = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Issue, pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = self.issue
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.issue
        return kwargs

    def form_valid(self, form):
        types = form.cleaned_data.pop('issue_type')
        issue = form.save()
        issue.issue_type.set(types)
        return redirect('issue_detail', pk=issue.pk)


class IssueDeleteView(View):
    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=self.kwargs.get('pk'))
        issue.delete()
        return redirect('issue_list')