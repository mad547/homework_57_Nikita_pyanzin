from django.contrib import admin
from tracker_app.models import Type, Status, Issue, Project


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'project','is_deleted' , 'created_at',]
    list_filter = ['status', 'project', 'is_deleted']
    search_fields = ['summary']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_date', 'end_date',]
    search_fields = ['name', 'description']
    filter_horizontal = ['members']

admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Issue, IssueAdmin)