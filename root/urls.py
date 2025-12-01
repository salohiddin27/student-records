from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from main.middleware import (custom_404, custom_400, custom_401, custom_403,
                             custom_405, custom_408)

urlpatterns = [
    path('', include('main.urls')),
    path('login/', admin.site.urls),
    path('api-token-auth', obtain_auth_token),

]

handler400 = custom_400
handler401 = custom_401
handler403 = custom_403
handler404 = custom_404
handler405 = custom_405
handler408 = custom_408
