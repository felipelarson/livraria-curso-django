from rest_framework.serializers import ModelSerializer

from Autor.models import Autor


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"
