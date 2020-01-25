from rest_framework import viewsets, serializers
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'created')


class PostPagination(LimitOffsetPagination):
    default_limit = 5


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = (OrderingFilter,)
    ordering = ('-created', '-id')
    queryset = Post.objects.all()
