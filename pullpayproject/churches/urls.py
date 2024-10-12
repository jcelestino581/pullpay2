from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("edit_church_screen", views.edit_church_screen, name="edit_church_screen"),
    path("view_churches/", views.view_churches, name="view_churches"),
    path("add_church/", views.add_church, name="add_church"),
    path("delete_church/<int:id>/", views.delete_church, name="delete_church"),
    path("update_church/<int:id>/", views.update_church, name="update_church"),
    path("create_user", views.create_user, name="create_user"),
    path("user_list/", views.user_list, name="user_list"),
    path("success/", views.success, name="success"),
    path("register/", views.register, name="register"),
    path(
        "login_view/",
        auth_views.LoginView.as_view(template_name="Login/login_view.html"),
        name="login_view",
    ),
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="login_view"), name="logout"
    ),
]
