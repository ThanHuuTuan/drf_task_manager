from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import Project
from projects.serializers import ProjectSerializer
from system.permissions import ManagerOrAdminOrReadOnly


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (ManagerOrAdminOrReadOnly,)


class JoinProjectView(APIView):

    def post(self, request, project_pk, format=None):
        project_obj = Project.objects.filter(id=int(project_pk)).first()
        if project_obj:
            project_obj.users.add(request.user.id)
            project_obj.save()
        serializer = ProjectSerializer(project_obj)

        return Response(serializer.data)
