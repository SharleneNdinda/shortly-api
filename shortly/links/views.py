from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from shortly.links.models import Link
from shortly.links.serializers import LinkSerializer


class LinkViewSet(ModelViewSet):
    """Link ViewSet."""

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]
