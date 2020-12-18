from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('drf.urls')),
    path('usercomment/', include('usercomment.urls')),
    # rest api 상에서 로그인 로그아웃이 가능하도록 하기
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),

]
