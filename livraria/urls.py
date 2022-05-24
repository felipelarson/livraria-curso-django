from core import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("teste/", views.teste),
    path("categorias/", views.CategoriaView.as_view()),
    path("categorias/<int:id>/", views.CategoriaView.as_view()),
    path("categorias-apiview/", views.CategoriaView.as_view()),
    path("categorias-apiview/<int:id>/", views.CategoriaDetail.as_view()),
]
