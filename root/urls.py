from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from main.middleware import custom_404

urlpatterns = [
    path('', include('main.urls')),
    path('login/', admin.site.urls),
    path('api-token-auth', obtain_auth_token),

]

handler404 = custom_404
