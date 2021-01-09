# ––– DJANGO IMPORTS
from django.db import models
from django.http import HttpResponse


# ––– PYTHON UTILITY IMPORTS
import csv


# –––THIRD-PARTY IMPORTS
import ulid


# ––– PROJECT IMPORTS


# ––– PARAMETERS


# ––– MODELS


def generate_ulid():
    return str(ulid.ULID())


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class AbstractBaseModel(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=26,
        default=generate_ulid,
        unique=True,
        blank=True,
        editable=False,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        abstract = True