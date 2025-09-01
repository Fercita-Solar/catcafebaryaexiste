from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('noticias-ofertas/', views.news_sales, name='news_sales'),
    path('galeria/', views.galeria, name='galeria'),
]