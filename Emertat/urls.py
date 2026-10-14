from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from info import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),

    path('', include('info.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
