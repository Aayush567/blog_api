from rest_framework import generics
from posts.models import Post
from posts.api.serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsOwnerOrReadOnly
from django.db.models import Q
from rest_framework import filters
from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination


"""This is list of all post """
class PostListAPIView(generics.ListAPIView):

    serializer_class = PostListSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ['username', 'title','content','slug','user__first_name']
    pagination_class = PostPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list

''' Return details of post list '''
class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    #lookup_url_kwarg = 'abc'
    permission_classes = [AllowAny]

''' Delete indivisual post from post list '''
class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    '''
    below permission comment because we have set default permission class in setting as IsAuthenticated
    so we dont required any more permission class here 
    
    '''
    #permission_classes = (IsAuthenticated,)

''' create new post list by authenticated user '''
class PostCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    #permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

''' update post whome this '''
class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)









