from dropship import models
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = "__all__"


class StandardUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StandardUser
        fields = "__all__"


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Issue
        fields = "__all__"