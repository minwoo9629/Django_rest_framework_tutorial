from rest_framework import viewsets
from .models import UserComment
from .serializers import UserCommentSerializer
# search 기능
from rest_framework.filters import SearchFilter 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser

class UserCommentViewSet(viewsets.ModelViewSet):
    # 내가 적용하고자 하는 authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer

    filter_backends = [SearchFilter]
    # 어떤 column을 기반으로 검색을 할 건지 작성한다. -> 튜플로 작성
    serach_fields = ('subject',)

    def get_queryset(self):
        # 내부에서 쿼리셋을 조작한다.
        # 부모 클래스의 queryset을 가져옴
        qs = super().get_queryset()

        # 지금 로그인한 유저의 글만 filtering 로그인 안한 경우 아무것도 보여주지않음
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()
        
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)