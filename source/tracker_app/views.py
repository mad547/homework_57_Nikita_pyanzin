from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from tracker_app.models import Issue
from tracker_app.forms import IssueForm


# Create your views here.
class IssueListView(View):
    def get(self, request):
        issue = Issue.objects.all()
        return render(request, 'tracker_app/issue_list.html', {'issue': issue})


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
            issue = form.save()
            return redirect('issue_detail', pk=issue.pk)
        return render(request, 'tracker_app/issue_create.html', {'form': form})


class IssueUpdateView(View):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(instance=issue)
        return render(request, 'tracker_app/issue_update.html', {'form': form, 'issue': issue})

    def post(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
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