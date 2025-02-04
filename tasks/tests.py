from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken


class ListCreateTasksTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.access_token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            user=self.user  
        )
        
    def test_retrieve_tasks_list(self):
        url = reverse('tasks:api_tasks_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_create_task(self):
        url = reverse('tasks:api_tasks_list')
        data = {
            'title': 'Create Test Task',
            'description': 'Create Test Description',
            'completed': False,
            'user': self.user.id
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TaskDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            user=self.user  
        )
        
    def test_retrieve_task(self):
        url = reverse('tasks:api_task_detail', kwargs={'pk': self.task.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_update_task(self):
        url = reverse('tasks:api_task_detail', kwargs={'pk': self.task.id})
        data = {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'completed': True,
            "user": self.user.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_delete_task(self):
        url = reverse('tasks:api_task_detail', kwargs={'pk': self.task.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())