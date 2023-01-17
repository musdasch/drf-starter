from django.contrib.auth.models import User
from .models import Task
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer
from .serializers import TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all();
    serializer_class = TaskSerializer;
