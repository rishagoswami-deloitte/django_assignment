from dropship import models
from dropship import serializers
from rest_framework import viewsets


class StandardUserModelViewSet(viewsets.ModelViewSet):
    queryset = models.StandardUser.objects.all()
    serializer_class = serializers.StandardUserSerializer


class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class IssueModelViewSet(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer

    