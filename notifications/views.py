from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
# from rest_framework.decorators import action 
from rest_framework import viewsets

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # @action(detail=True, methods=['post']) # ata kno dese oita larn korta hova .. .. .. 
    # def like(self, request, pk):   
    #     post=self.get_object()
    #     return Response(
    #         {"message": "Post liked successfully"},
    #         status=status.HTTP_200_OK
    #     ) 