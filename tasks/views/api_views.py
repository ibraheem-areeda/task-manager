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

class TaskDetailView(APIView):
    """
     Retrieve, update, or delete a task by ID.
    """
    @swagger_auto_schema(
        operation_description="Retrieve a Task by ID.",
        responses={200: TaskSerializer(many=True)},
        security=[]
    )
    def get(self, request, pk, format=None):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        
    @swagger_auto_schema(
        operation_description="update a Task by ID.",
        request_body=TaskSerializer,
        responses={202: TaskSerializer, 400: "Bad Request"},
        security=[]
    )
    def put(self, request, pk, format=None):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="delete a Task by ID.",
        responses={200: "task with id '5' successfully deleted", 404: "Task not found"},
        security=[]
    )
    def delete(self, request, pk, format=None):
        try:
            task = Task.objects.get(pk=pk)
            task.delete()
            return Response({"msg":f"task with id '{pk}' successfully deleted"},status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)