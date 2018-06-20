from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from comments.models import Comment
from comments.api.serializers import CommentListSerializer, CommentDetailSerializer


class CommentListAPIView(APIView):


    def get(self, request, format=None):
        comment = Comment.objects.all()
        serializer = CommentListSerializer(comment, many=True)
        print(serializer)
        return Response(serializer.data)

class CommentDetailAPIView(APIView):

    def get(self, request, pk):
        comment = Comment.objects.filter(id=pk)
        serializer = CommentDetailSerializer(comment, many=True)
        return Response(serializer.data)

