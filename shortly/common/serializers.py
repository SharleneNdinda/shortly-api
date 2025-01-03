from rest_framework.serializers import ModelSerializer

from shortly.links.models import Link


class BaseSerializer(ModelSerializer):
    """Base Serializer for other apps."""
    
    def create():
        """Custom `create` method containing additional functionality."""