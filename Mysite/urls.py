from django.contrib import admin
from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
