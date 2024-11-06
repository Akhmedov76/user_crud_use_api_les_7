from rest_framework import serializers

from app_blogs.models import UsersModel


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'

