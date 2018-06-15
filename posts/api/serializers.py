from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField
from posts.models import Post

detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug',
)

delete_url = HyperlinkedIdentityField(
    view_name ='posts-api:delete',
    lookup_field='slug',
)

class PostListSerializer(serializers.ModelSerializer):
    detail_url = detail_url
    delete_url = delete_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','user','image','detail_url','slug','title','html','content','publish','delete_url','delete_url']

    def get_html(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image

class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id','user','slug','title','content','publish']




