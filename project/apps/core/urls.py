from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, register_converter

from apps.core import converters

register_converter(converters.ULIDConverter, "ulid")
app_name = "apps.core"

urlpatterns = [

]
