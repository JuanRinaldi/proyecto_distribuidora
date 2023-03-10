
from django.contrib import admin
from django.urls import path
from . import views
from productos.views import ProductListView
from django.urls import include
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view() , name='index'),
    path('usuarios/login' , views.login_views, name='login'),
    path('usuarios/logout' , views.logout_views, name='logout'),
    path('usuarios/registro', views.registro , name="registro"),
    path('productos/', include('productos.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)