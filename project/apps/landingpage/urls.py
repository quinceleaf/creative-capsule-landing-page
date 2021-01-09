from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, register_converter

from apps.core import converters
from apps.landingpage import views

register_converter(converters.ULIDConverter, "ulid")
app_name = "apps.landingpage"

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.index, name="index"),
]
