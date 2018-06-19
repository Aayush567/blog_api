from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from posts.api.pagination import PostLimitOffsetPagination, PostPageNumberPagination
from django.contrib.auth import get_user_model
from accounts.api.serializers import UserCreateSerializer, UserLoginSerializer
User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self,request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            new_data = serializer.data
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

