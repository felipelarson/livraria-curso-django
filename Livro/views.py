from rest_framework.viewsets import ModelViewSet

from Livro.models import Livro
from Livro.serializers import LivroDetailSerializer, LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroDetailSerializer
        if self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
