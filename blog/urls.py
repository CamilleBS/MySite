from django.urls import include,path
from . import views

app_name ="blog"
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.detail, name='post_detail'),
    path('new_post', views.post_new, name='new_post'),
]