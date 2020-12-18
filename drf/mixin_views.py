from .models import Comment
from .serializers import CommentSerializer
"""
코드의 불필요한 반복(코드의 낭비)을 줄이기위해 CBV의 장점인 상속을 이용
"""
from rest_framework import mixins
from rest_framework import generics

# mixins를 이용
class CommentListMixins(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    """
    깃허브에서 mixins ListModelMixin 내용을 확인해보면
    comment = Comment.objects.all()    
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data) 과 유사하다는 걸 알 수 있다.
    CreateModelMixin도 확인해보면 알 수 있다.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CommentDetailMixins(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    """
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)