from tracker_app.vievs.issue_views import (
IssueListView,
IssueDetailView,
IssueCreateView,
IssueUpdateView,
IssueDeleteView,
)

from tracker_app.vievs.project_views import (
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
    'IssueCreateView',
    'IssueUpdateView',
    'IssueDeleteView',
    'ProjectListView',
    'ProjectDetailView',
    'ProjectCreateView',
    'ProjectUpdateView',
    'ProjectDeleteView',
    'ProjectIssueCreateView',
]