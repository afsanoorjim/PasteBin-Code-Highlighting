from .models import Snippets
from .serializers import SnippetsSerializers, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetsList(generics.ListCreateAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsSerializers


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]