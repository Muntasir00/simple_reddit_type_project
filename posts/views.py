from django.shortcuts import render
from posts import serializers
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post
# Create your views here.
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user) 