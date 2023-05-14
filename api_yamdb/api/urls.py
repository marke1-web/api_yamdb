from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    SignUPView,
    TokenView,
    UserViewSet,
)


router = DefaultRouter()


router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('auth/signup/', SignUPView.as_view()),
    path('auth/token/', TokenView.as_view()),
    path('', include(router.urls)),
]
