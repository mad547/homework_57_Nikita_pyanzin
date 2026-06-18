from django.urls import path
from tracker_app.views import (
    IssueListView, IssueDetailView, IssueUpdateView, IssueDeleteView,
    ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView,
    ProjectIssueCreateView,
)


urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:project_pk>/issues/create/', ProjectIssueCreateView.as_view(), name='project_issue_create'),

    path('issues/', IssueListView.as_view(), name='issue_list'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('issues/<int:pk>/update/', IssueUpdateView.as_view(), name='issue_update'),
    path('issues/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
]