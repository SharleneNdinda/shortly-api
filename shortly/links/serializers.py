from rest_framework.serializers import ModelSerializer

from shortly.links.models import Link


class LinkSerializer(ModelSerializer):
    """Link Serializer."""

    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = ["short_url", "short_url_id", "user"]
