from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from shortly.links.models import Link
from shortly.links.serializers import LinkSerializer


class LinkViewSet(ModelViewSet):
    """Link ViewSet."""

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False)
    def homepage(self, request):
        return  render(request=request,
        template_name= 'home.html')
