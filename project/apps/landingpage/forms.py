from django import forms

from apps.core import models as core_models
from apps.core.forms import BaseModelForm
from apps.landingpage import models


class SignupForm(BaseModelForm):
    def clean_email(self):
        objs = models.Signup.objects.all()
        if self.instance.id:
            objs = objs.exclude(id=self.instance.id)

        email = self.cleaned_data["email"]
        if objs.filter(email=email).exists():
            raise forms.ValidationError("You've already registered with that email")
        return email

    class Meta:
        model = models.Signup
        fields = ("email",)
