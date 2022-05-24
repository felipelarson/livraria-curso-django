from core import views
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"categorias-viewset", views.CategoriaViewSet)

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path("teste/", views.teste),
    # path("categorias/", views.CategoriaView.as_view()),
    # path("categorias/<int:id>/", views.CategoriaView.as_view()),
    # path("categorias-apiview/", views.CategoriaView.as_view()),
    # path("categorias-apiview/<int:id>/", views.CategoriaDetail.as_view()),
    # path("categorias-generic/", views.CategoriaListGeneric.as_view()),
    # path(
    #     "categorias-generic/<int:id>/", views.CategoriaDetailGeneric.as_view()
    # ),
    path("", include(router.urls)),
]
