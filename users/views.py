from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from system.permissions import ManagerOrAdminOrReadOnly
from users.models import User
from users.serializers import UserSerializer


class UsersRegistrationView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class DevelopersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ManagerOrAdminOrReadOnly,)

    def get_queryset(self):
        return self.queryset.filter(role='developer')
