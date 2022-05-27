from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.URLField()

    def __str__(self):
        return "%s (%s)" % (self.nome, self.site)
