# LandingPage URL Configuration

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("django.contrib.auth.urls")),
    path("core/", include("apps.core.urls", namespace="core")),
    path("", include("apps.landingpage.urls", namespace="landingpage")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "LandingPage Administration"
admin.site.site_title = "LandingPage Administration"
admin.site.index_title = "LandingPage Administration"
