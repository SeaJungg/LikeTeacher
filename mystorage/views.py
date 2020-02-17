from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters import SearchFilter

class PostviewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title','school')
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

        #현재 request를 보낸 유저
        # self.request.user

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            # 어드민일 경우 모든 글 보기..가 안되네여
            # if self.request.user == 'admin' :
            #    qs = qs.all()
            #else:
            qs = qs.filter(author = self.request.user)
        else:
            qs = qs.none()
        return qs
        
class ImgviewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class FileviewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer