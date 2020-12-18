from rest_framework import serializers
from .models import UserComment
class UserCommentSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    class Meta:
        model = UserComment
        fields = ['pk','subject','content','author_name']


