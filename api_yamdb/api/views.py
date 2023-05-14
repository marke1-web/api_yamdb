
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework import (
    filters,
    mixins,
    viewsets,
)

from api.filters import TitlesFilter
from api.permissions import ReadOnly, AdminRules
from api.serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleCreateUpdateSerializer,
    TitleSerializer,
)
from reviews.models import Category, Genre, Title


HTTP_METHOD = ('get', 'post', 'patch', 'delete')


class ListCreateDestroyViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    pass


class CategoriesViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnly | AdminRules]
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    lookup_field = 'slug'
    ordering = ('id',)


class GenresViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [ReadOnly | AdminRules]
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name',)
    ordering = ('id',)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [ReadOnly | AdminRules]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    http_method_names = HTTP_METHOD
    filterset_class = TitlesFilter
    ordering = ('id',)

    def get_serializer_class(self):
        if self.action in ['create', 'partial_update']:
            return TitleCreateUpdateSerializer
        return TitleSerializer