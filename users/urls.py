from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token, ObtainJSONWebToken
from users.views import UsersRegistrationView, DevelopersView

router = routers.SimpleRouter()
router.register('registration', UsersRegistrationView)  # register new user using email and password
router.register('users/developers', DevelopersView)  # CRUD for users-developers

urlpatterns = [
    path('', include(router.urls)),
    path('auth/refresh/', refresh_jwt_token),
    path('auth/verify/', verify_jwt_token),
    path('auth/', ObtainJSONWebToken.as_view()),  # get token by POST email and password of existing user
]
