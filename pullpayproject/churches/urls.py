from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("top/", views.topChurches, name="topChurches"),
    path('add_church/', views.add_church, name='add_church'),
    path('success/', views.success, name='success'),
]
