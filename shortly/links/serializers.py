from rest_framework.serializers import ModelSerializer

from shortly.common.views import BaseSerializer
from shortly.links.models import Link


class LinkSerializer(BaseSerializer):
    """Link Serializer."""

    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = ["short_url", "short_url_id", "user"]
