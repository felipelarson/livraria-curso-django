from Editora.models import Editora
from rest_framework.serializers import ModelSerializer


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"


class EditoraNestedSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = (
            "nome",
            "site",
        )
