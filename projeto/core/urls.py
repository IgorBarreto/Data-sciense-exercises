from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('projeto1.urls')),
    path('', include('projeto2.urls')),
    path('', include('projeto3.urls')),
    path('', include('projeto4.urls')),
    path('', include('projeto5.urls')),
    path('', include('projeto6.urls')),
]
# Configuração para arquivos estáticos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Configuração para arquivos de mídia
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
