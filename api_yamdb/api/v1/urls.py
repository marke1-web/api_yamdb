from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import (
    CategoriesViewSet,
    CommentViewSet,
    GenresViewSet,
    ReviewViewSet,
    SignUPView,
    TitlesViewSet,
    TokenView,
    UserViewSet,
)


router = DefaultRouter()

router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router.register('categories', CategoriesViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path(
        'auth/',
        include(
            [
                path('signup/', SignUPView.as_view()),
                path('token/', TokenView.as_view()),
            ]
        ),
    ),
    path('', include(router.urls)),
]
