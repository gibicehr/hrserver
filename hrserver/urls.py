from django.contrib import admin
from django.urls import include, path, re_path


urlpatterns = [
    path('info/', include('info.urls')),
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    re_path(r'.*', include('index.urls')),
]
