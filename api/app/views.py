from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Post
from app.serializers import PostSerializer


@api_view(['GET','POST'])
def post_create_and_get(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        post_serializer = PostSerializer(posts, many=True)
        return Response(post_serializer.data)
    
    elif request.method == 'POST':
        post_serializer = PostSerializer(data=request.data)
        
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data,status=status.HTTP_201_CREATED)

        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH','DELETE'])
def post_edit_and_delete(request, id):
    try:
        post = Post.objects.get(pk=id)

    except Post.DoesNotExist:
        return  Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PATCH':
        post_serializer = PostSerializer(post, data=request.data,partial=True)
        
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data,status=status.HTTP_200_OK)
        
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response({},status=status.HTTP_204_NO_CONTENT)