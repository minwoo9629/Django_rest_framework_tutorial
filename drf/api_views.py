from .models import Comment
from .serializers import CommentSerializer
"""
APIView를 상속하여 View를 설계 할 땐

status와 Response를 import해와서 직접 응답과정을 만든다.

HTTP404를 직접 구현을 위해 Http404 import

from django.shortcuts import get_object_or_404를 사용해도 된다.

"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# apiview를 이용해 직접 method 정의
class CommentList(APIView):
    def get(self, request, format=None):
        # 모든 객체들의 쿼리셋을 가져옴
        comment = Comment.objects.all()
        # 다수의 객체를 serializer를 위해 many=True 인자
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """
        request.POST  # Only handles form data.  Only works for 'POST' method.
        request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
        """
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)