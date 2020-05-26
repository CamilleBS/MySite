from django.contrib import admin
from django.urls import include,path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/', include('blog.urls')),
    path('diy/', include('diy.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
