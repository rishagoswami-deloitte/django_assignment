from dropship import models
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = "__all__"


class StandardUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StandardUser
        fields = ('id', 'f_name', 'l_name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create_user(self, validated_data):
        user = models.User.objects.create_user(
            validated_data['email'], validated_data['email'], validated_data['password'])
        obj = models.StandardUser.objects.create(
            first_name=validated_data['f_name'],
            last_name=validated_data['l_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            user=user
        )
        return obj

    def update_user(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        obj = models.StandardUser.objects.get(id=instance.id)
        return super().update(obj, validated_data)


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Issue
        fields = "__all__"