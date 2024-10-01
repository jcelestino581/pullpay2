from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view_churches/", views.view_churches, name="view_churches"),
    path("add_church/", views.add_church, name="add_church"),
    path("delete_church/<int:id>/", views.delete_church, name="delete_church"),
    path("update_church/<int:id>/", views.update_church, name="update_church"),
    path("success/", views.success, name="success"),
]
