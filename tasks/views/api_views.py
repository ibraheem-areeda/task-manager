from ..models import Task
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..serializers import TaskSerializer


class ListCreateTasks(APIView):
    """
    A view to list all Tasks or create a new Task.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get a list of all Tasks",
        responses={200: TaskSerializer(many=True)},
    )
    def get(self, request, format=None):
        """
        Handle GET requests to list all users.
        """
        users = Task.objects.all()
        serializer = TaskSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new Task",
        request_body=TaskSerializer,
        responses={201: TaskSerializer, 400: "Bad Request"},
    )
    def post(self, request, format=None):
        """
        Handle POST requests to create a new user.
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
