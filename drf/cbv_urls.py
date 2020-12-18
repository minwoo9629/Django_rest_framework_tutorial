from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
# Default Router 사용 x => API ROOT 없음.
urlpatterns = [
    # http://127.0.0.1:8000/comment/ == ListView 
    path('comment/', views.CommentList.as_view()),
    # http://127.0.0.1:8000/comment/pk값  == DetailView
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('comment/mixins/', views.CommentListMixins.as_view()),
    path('comment/mixins/<int:pk>/', views.CommentDetailMixins.as_view()),
    path('comment/generics/', views.CommentListMixins.as_view()),
    path('comment/generics/<int:pk>', views.CommentDetailMixins.as_view()),

]

"""
http http://127.0.0.1:8000/comment.json  # JSON suffix
http http://127.0.0.1:8000/comment.api   # Browsable API suffix
"""
urlpatterns = format_suffix_patterns(urlpatterns)