#장고 웹서비스를 만들 때 form과 비슷한 역할을 한다
from .models import Essay, Album, Files
from rest_framework import serializers

class EssaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name','school')

class FilesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    myfile = serializers.FileField(use_url = True)
    class Meta:
        model = Album
        fields = ('pk','author_name','files','desc')

class AlbumSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url = True)
    class Meta:
        model = Album
        fields = ('pk','author_name','image','desc')
