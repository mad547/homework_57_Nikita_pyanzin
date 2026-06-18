from tracker_app.views.issue_views import (
IssueListView,
IssueDetailView,
IssueUpdateView,
IssueDeleteView,
)

from tracker_app.views.project_views import (
ProjectListView,
ProjectDetailView,
ProjectCreateView,
ProjectUpdateView,
ProjectDeleteView,
ProjectIssueCreateView,
)

__all__ = [
    'IssueListView',
    'IssueDetailView',
    'IssueUpdateView',
    'IssueDeleteView',
    'ProjectListView',
    'ProjectDetailView',
    'ProjectCreateView',
    'ProjectUpdateView',
    'ProjectDeleteView',
    'ProjectIssueCreateView',
]