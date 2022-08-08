from rest_framework.views import APIView
from rest_framework.response import Response
from dropship import models
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken


class CustomAuthToken(ObtainAuthToken):
    def addeditem(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        try:
            member_obj = models.Member.objects.get(user=user.pk)
        except:
            print("User Doesn't Exist")
        return Response({
            'first_name': member_obj.first_name,
            'last_name': member_obj.last_name,
        })