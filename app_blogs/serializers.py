from rest_framework import serializers

from app_blogs.models import UsersModel, BlogsModel


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsModel
        fields = '__all__'
