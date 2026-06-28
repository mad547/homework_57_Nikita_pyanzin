from django.contrib.auth.mixins import UserPassesTestMixin


class ProjectMemberMixin(UserPassesTestMixin):
    def get_project(self):
        raise NotImplementedError

    def test_func(self):
        project = self.get_project()
        return project.members.filter(pk=self.request.user.pk).exists()