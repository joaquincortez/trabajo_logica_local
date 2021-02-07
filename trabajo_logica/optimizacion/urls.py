from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('optimizacion/', views.optimizacion, name='optimizacion'),
    path('calculoshelado/', views.calculos_helado, name='calculos_helado'),
    path('calculosmateria/', views.calculos_materia, name='calculos_materia'),
    path('calculos/', views.calculos, name='calculos'),
    path('scheduling/', views.scheduling, name='scheduling'),
    path('packing/', views.packing, name='packing'),
]