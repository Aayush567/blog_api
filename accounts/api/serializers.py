from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField



User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    email2 = serializers.EmailField(label='Confirm Email')
    email = serializers.EmailField(label='Email Address')

    class Meta:
        model = User
        fields = ['username','email','email2','password']
        extra_kwargs ={'password':{'write_only':True}}

    # def validate(self, data):
    #     email = data['email']
    #     user_qs = User.objects.filter(email=email)
    #     if user_qs.exists():
    #         raise serializers.ValidationError('This user is already register')
    #     return data



    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = data.get('email2')
        if email2 != email1:
            raise serializers.ValidationError("Email must be match")
        user_qs = User.objects.filter(email=email1)
        if user_qs.exists():
            raise serializers.ValidationError("User already exists")
        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = data.get('email2')
        if email2 != email1:
            raise serializers.ValidationError("Email must be match")
        return value

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank = True, read_only = True)
    email = serializers.EmailField(label= 'Email Address', required = False, allow_blank=True)
    username = serializers.CharField(required = False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'email','token','password']

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        if not email and not username:
            raise serializers.ValidationError("Please provide any one username or email")
        return data