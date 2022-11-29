from django.urls import path
from . import views
urlpatterns = [
    path('daddy/', views.muestra_datos, name='daddy'),
    path('knn/', views.muestra_datos, name='knn'),
    path('algoritmo1/', views.algKNN, name='algoritmo1'),
    path('algoritmoBaye/', views.algBaye, name='algoritmoBaye'),
    path('RALineal/', views.RLineal, name='RALineal'),
]
