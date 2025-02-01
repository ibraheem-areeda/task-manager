from django.http import HttpResponse
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from ..serializers import  UserSerializer
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response


    
class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
   