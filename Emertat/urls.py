from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from info import views


# URLs that should NOT have a language prefix
urlpatterns = [
    path('admin/', admin.site.urls),

    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),

    # Django language switching endpoint
    path('i18n/', include('django.conf.urls.i18n')),
]


# Website pages
urlpatterns += i18n_patterns(
    path('', include('info.urls')),

    prefix_default_language=False
)


urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
