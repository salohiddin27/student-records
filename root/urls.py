from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('main.urls')),
    path('login/', admin.site.urls),
    path('api-token-auth', obtain_auth_token),

]

