from rest_framework import serializers
from comments.models import Comment

class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id','user', 'content','object_id','parent','content_type']

class CommentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'user','content','object_id','parents', 'content_type']


