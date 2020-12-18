from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework import permissions


"""
@action 처리를 위한 import
"""
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse
"""
Pagination 처리
"""

from .pagination import Mypagination
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

# 읽기 기능만을 수행하는 View가 필요할 경우
# class CommentViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # pagination 코드 추가
    pagination_class = Mypagination
    """
    액션을 수행할 수 있는 권한 설정하기
    IsAuthenticatedOrReadOnly : 인증된 요청에 대해서만 권한 부여 / 비인증 요청은 읽기 권한
    IsOwnerOrReadOnly : 소유인사람 권한부여 / 소유자가 아니면 읽기 기능
    ex : permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

     CRUD를 제외한 커스텀 API를 작성하기
     @ + 함수들 -> decorator
     renderer_classes : 함수의 response 객체를 어떤 방식으로 rendering 할 것인가
     renderer.JSONRender, renderer.BrowsableAPIRenderer 등
     기본 method == GET
     @action(method=['post]) : POST로 사용할 경우
     """
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        # 직접 Response 만들기
        return HttpResponse("highlight 메소드 결과")