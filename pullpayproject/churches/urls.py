from django.urls import path
from django.contrib.auth import views as auth_views

# from django.urls import path
from . import views
from churches.views import *

urlpatterns = [
    path("", views.index, name="index"),
    path("home", ReactView.as_view(), name="home"),
    path("index/", views.index, name="index"),
    path("edit_church_screen", views.edit_church_screen, name="edit_church_screen"),
    path("view_churches/", views.view_churches, name="view_churches"),
    path("add_church/", views.add_church, name="add_church"),
    path("delete_church/<int:id>/", views.delete_church, name="delete_church"),
    path("update_church/<int:id>/", views.update_church, name="update_church"),
    path("create_user", views.create_user, name="create_user"),
    path("user_list/", views.user_list, name="user_list"),
    path("success/", views.success, name="success"),
    # path("register/", views.register, name="register"),
    path(
        "login_view/",
        auth_views.LoginView.as_view(template_name="Login/login_view.html"),
        name="login_view",
    ),
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="login_view"), name="logout"
    ),
    path("view_profile", views.view_profile, name="view_profile"),
    path("create_transaction", views.create_transaction, name="create_transaction"),
    path("view_transactions", views.view_transactions, name="view_transactions"),
    path("register/", RegisterView.as_view(), name="register"),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/user-dashboard/", user_dashboard, name="user_dashboard"),
]
