from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from tracker_app.models import Issue
from tracker_app.forms import IssueForm


class IssueListView(View):
    def get(self, request):
        issues = Issue.objects.all()
        return render(request, 'tracker_app/issue_list.html', {'issues': issues})


class IssueDetailView(View):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        return render(request, 'tracker_app/issue_detail.html', {'issue': issue})


class IssueCreateView(View):
    def get(self, request):
        form = IssueForm()
        return render(request, 'tracker_app/issue_create.html', {'form': form})

    def post(self, request):
        form = IssueForm(request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('issue_type')
            issue = form.save()
            issue.issue_type.set(types)
            return redirect('issue_detail', pk=issue.pk)
        return render(request, 'tracker_app/issue_create.html', {'form': form})


class IssueUpdateView(View):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(instance=issue, initial={'issue_type': issue.issue_type.all()})
        return render(request, 'tracker_app/issue_update.html', {'form': form, 'issue': issue})

    def post(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            types = form.cleaned_data.pop('issue_type')
            form.save()
            issue.issue_type.set(types)
            return redirect('issue_detail', pk=issue.pk)
        return render(request, 'tracker_app/issue_update.html', {'form': form, 'issue': issue})


class IssueDeleteView(View):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        return render(request, 'tracker_app/issue_delete.html', {'issue': issue})

    def post(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('issue_list')