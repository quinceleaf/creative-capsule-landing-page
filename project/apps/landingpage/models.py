# ––– DJANGO IMPORTS
from django.db import models


# ––– PYTHON UTILITY IMPORTS


# –––THIRD-PARTY IMPORTS


# ––– PROJECT IMPORTS
from apps.core import models as core_models


# ––– PARAMETERS


# ––– MODELS


# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# SIGNUP
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––


class Signup(core_models.AbstractBaseModel):

    email = models.CharField(max_length=150, unique=True)
    is_mailchimp_successful = models.BooleanField(default=False)
    mailchimp_id = models.CharField(max_length=24, null=True, blank=True)
    mailchimp_ip_registration = models.CharField(max_length=24, null=True, blank=True)
    mailchimp_error = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.email}"
