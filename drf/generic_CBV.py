from .models import Comment
from .serializers import CommentSerializer
from rest_framework import generics

class CommentListGeneric(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer