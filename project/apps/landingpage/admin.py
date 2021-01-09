from django.contrib import admin

from apps.core.admin import BaseAdminConfig
from apps.landingpage import models


@admin.register(models.Signup)
class SignupAdmin(BaseAdminConfig):
    pass