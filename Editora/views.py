from rest_framework.viewsets import ModelViewSet
from Editora.models import Editora

from Editora.serializers import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
