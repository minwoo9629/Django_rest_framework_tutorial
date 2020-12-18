from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        # 전체를 선택할 경우
        # fields = '__all__'
        fields = ['id','subject','content']
        """
        read_only로 설정하고 싶을 때
        OPTIONS에서 read_only가 true인 것을 확인 할 수 있다.
        read_only_fields = ('subject',)
        """
