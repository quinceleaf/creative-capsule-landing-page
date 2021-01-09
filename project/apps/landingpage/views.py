# ––– DJANGO IMPORTS
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView


# ––– PYTHON UTILITY IMPORTS
import os


# ––– THIRD-PARTY IMPORTS
import dotenv
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


# ––– APPLICATION IMPORTS
from apps.core import models as core_models
from apps.landingpage import models


"""
Views for
Index
"""

# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# SUBSCRIPTION
# –––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

dotenv.load_dotenv()
API_KEY = os.getenv("MAILCHIMP_API_KEY", None)
API_DATACENTER = os.getenv("MAILCHIMP_API_DATACENTER", None)
API_LIST_ID = os.getenv("MAILCHIMP_API_LIST_ID", None)


def submit_to_mailchimp(email):
    """
    Adds email as contact on MailChimp audience/list via MailChimp API
    """
    mailchimp = Client()
    mailchimp.set_config(
        {
            "api_key": API_KEY,
            "server": API_DATACENTER,
        }
    )

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(API_LIST_ID, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        response = {"status": error.text}
        print("An exception occurred: {}".format(error.text))

    return response


def index(request):

    """
    Serves form for signup via email and submits to MailChimp
    """

    if request.method == "POST":
        email = request.POST.get("email", None)
        print(f"Email submitted: {email}")

        print(
            f"API_KEY, API_DATACENTER, API_LIST_ID: {API_KEY}, {API_DATACENTER}, {API_LIST_ID}"
        )

        # Submit to MailChimp
        if all([API_KEY, API_DATACENTER, API_LIST_ID, email]):
            existing_signup = models.Signup.objects.filter(email=email)
            if existing_signup:
                print(f"Email {email} already signed up")
                return render(request, "success.html")

            try:
                print("Attempting MailChimp API post")
                res = submit_to_mailchimp(email)
                if res["status"] == "subscribed":
                    print("Email added to MailChimp")
                    signup = models.Signup.objects.create(
                        email=email,
                        is_mailchimp_successful=True,
                        mailchimp_id=res.get("unique_email_id", None),
                        mailchimp_ip_registration=res.get("ip_opt", None),
                    )
                    print(f"Signup id {signup.id} created")
                else:
                    print("Email NOT added to MailChimp")
                    signup = models.Signup.objects.create(
                        email=email,
                        is_mailchimp_successful=False,
                        mailchimp_error=res.get(
                            "status", "No information on error reported"
                        ),
                    )
                    print(f"Signup id {signup.id} created")
            except:
                print("Error occurred with no information; saving email")
                signup = models.Signup.objects.create(
                    email=email,
                    is_mailchimp_successful=False,
                    mailchimp_error=res.get(
                        "status", "No information on error reported"
                    ),
                )

        print("Fetching success.html")
        return render(request, "success.html")

    print("Fetching index.html")
    return render(request, "index.html")
