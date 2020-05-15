from django.urls import include,path
from . import views
from blog.views import PostList

urlpatterns = [
    path('', PostList.as_view()),
    path('posts/<id>', views.detail),
]