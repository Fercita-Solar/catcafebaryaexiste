from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', views.home, name='home'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('noticias-ofertas/', views.news_sales, name='preguntas_frecuentes'),
    path('galeria/', views.galeria, name='galeria'),
]