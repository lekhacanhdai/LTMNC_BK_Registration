from django.contrib import admin
from django.urls import path, include
from access_db import urls as access_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('bkdn/', include(access_url))
]
