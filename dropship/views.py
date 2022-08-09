from dropship import models
from dropship import serializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication  # TokenAuthentication ,
from rest_framework.permissions import IsAuthenticated


class StandardUserModelViewSet(viewsets.ModelViewSet):
    queryset = models.StandardUser.objects.all()
    serializer_class = serializers.StandardUserSerializer


class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class IssueModelViewSet(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class SprintModelViewSet(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]