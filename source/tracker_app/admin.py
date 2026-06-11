from django.contrib import admin
from tracker_app.models import Type, Status, Issue


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'issue_type', 'status', 'created_at',]
    list_filter = ['issue_type', 'status',]
    search_fields = ['summary']


admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Issue, IssueAdmin)