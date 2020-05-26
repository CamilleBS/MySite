from django.urls import include,path
from . import views

app_name = 'diy'
urlpatterns = [
    path('', views.sommaire, name='sommaire'),
    path('recettes', views.recettes, name='recettes'),
    path('recette_detail/<int:pk>/',views.recette_detail, name='recette_detail'),
    path('recette_edit',views.recette_edit, name='recette_edit')
]