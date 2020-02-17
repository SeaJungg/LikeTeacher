#장고 웹서비스를 만들 때 form과 비슷한 역할을 한다
from .models import Essay
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name','school')