from django.db import models

from shortly.authentication.models import User
from shortly.common.models import AbstractBase


class Link(AbstractBase):
    """Stores links generated by a User."""

    link = models.CharField()
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="user_links", null=True, blank=True
    )
    short_url = models.CharField(
        null=True, blank=True, help_text="URL generated from url shortener"
    )
    short_url_id = models.IntegerField(
        null=True, blank=True, help_text="Unique ID linked to shortened URL"
    )
