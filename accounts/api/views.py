from rest_framework import generics
from posts.models import Post
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsOwnerOrReadOnly
#from django.db.models import Q
from rest_framework import filters
from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination
from django.contrib.auth import get_user_model
from accounts.api.serializers import UserCreateSerializer
User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


