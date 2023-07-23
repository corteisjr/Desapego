
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('doeja.urls.AuthUrls')),
    path('', include('doeja.urls.HomeUrls')),
    path('profile/', include('doeja.urls.ProfileUrls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
