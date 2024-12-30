from django.db import models

from shortly.authentication.models import User
from shortly.common.models import AbstractBase


class UserLink(AbstractBase):
    """Ties a link back to a specific users."""

    link = models.CharField()
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="user_links",
    )
    short_url = models.CharField()
    short_url_id = models.IntegerField()
