from rest_framework.viewsets import ModelViewSet

from Autor.models import Autor
from Autor.serializers import AutorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
