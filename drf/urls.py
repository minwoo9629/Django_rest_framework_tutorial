from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# DRF는 router를 통해서 url를 결정한다.
router = DefaultRouter()
router.register('comment', views.CommentViewSet)
urlpatterns = [
    path('', include(router.urls)),
]