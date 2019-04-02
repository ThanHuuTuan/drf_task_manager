from django.conf.urls import url, include
from rest_framework import routers
from projects.views import ProjectView, JoinProjectView

router = routers.DefaultRouter()
router.register('projects', ProjectView)

urlpatterns = [
    url('', include(router.urls)),
    url(r'projects/(?P<project_pk>\d+)/join/', JoinProjectView.as_view()), #POST to join request.user to project by id
]
