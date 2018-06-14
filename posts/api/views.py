from rest_framework import generics
from posts.models import Post
from posts.api.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsOwnerOrReadOnly


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = 'abc'


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticated,)


class PostCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)









