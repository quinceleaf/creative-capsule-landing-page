from django.contrib import admin
from django.contrib.auth.admin import AdminPasswordChangeForm, UserAdmin
from django.utils.html import mark_safe

from apps.users import models
from apps.core.admin import admin_link, BaseAdminConfig


"""
User
"""


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# ADD-ONS
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# MODELS
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


class UserAdminConfig(BaseAdminConfig):
    fieldsets = (
        (
            "None",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "email",
                    "password",
                    "is_active",
                )
            },
        ),
        (
            "Last Login",
            {"fields": ("last_login",)},
        ),
        (
            "Groups & Permissions",
            {
                "fields": (
                    "groups",
                    "user_permissions",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
    ) + BaseAdminConfig.readonly_fieldsets
    filter_horizontal = ["groups", "user_permissions"]
    readonly_fields = ["id", "created_at", "last_login", "updated_at"]


# admin.site.unregister(models.User)


@admin.register(models.User)
class UserAdmin(UserAdminConfig):
    pass
