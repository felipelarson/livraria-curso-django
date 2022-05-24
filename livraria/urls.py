from core import views
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"autores", views.AutorViewSet)
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"compras", views.CompraViewSet)
router.register(r"editoras", views.EditoraViewSet)
router.register(r"livros", views.LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("teste/", views.teste),
    # path("categorias-class/", views.CategoriaView.as_view()),
    # path("categorias-class/<int:id>/", views.CategoriaView.as_view()),
    # path("categorias-apiview/", views.CategoriaView.as_view()),
    # path("categorias-apiview/<int:id>/", views.CategoriaDetail.as_view()),
    # path("categorias-generic/", views.CategoriaListGeneric.as_view()),
    # path(
    #     "categorias-generic/<int:id>/", views.CategoriaDetailGeneric.as_view()
    # ),
    path("", include(router.urls)),
]
