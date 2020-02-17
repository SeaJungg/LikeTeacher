from rest_framework.routers import DefaultRouter
from django.urls import path, include
from mystorage import views

router = DefaultRouter()
router.register('essay', views.PostviewSet)
router.register('album', views.ImgviewSet)
router.register('files', views.FileviewSet)

urlpatterns = [
    path('', include(router.urls)),
]