from Editora.views import EditoraViewSet
from Livro.views import LivroViewSet
from core import views
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"autores", views.AutorViewSet)
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"compras", views.CompraViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"livros", LivroViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    # Open API
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # Autenticação
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
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
