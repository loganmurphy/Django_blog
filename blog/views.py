# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from blog.models import Post
from blog.serializers import PostSerializer

@api_view(['GET'])
def post_list (request, slug):
    posts = Post.objects.filter(blog__slug=slug)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)