from rest_framework.viewsets import ModelViewSet

from Categoria.models import Categoria
from Categoria.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
