from django.urls import path
from tracker_app.views import (
IssueListView, IssueDetailView,
IssueCreateView, IssueUpdateView, IssueDeleteView
)


urlpatterns = [
    path('', IssueListView.as_view(), name='issue_list'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('issues/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issues/<int:pk>/update/', IssueUpdateView.as_view(), name='issue_update'),
    path('issues/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
]