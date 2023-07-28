from django.urls import path

from .views import create_post, home, sign_up

urlpatterns = [
    path("", home, name="home"),
    path("home", home, name="home"),
    path("sign-up", sign_up, name="sign-up"),
    path("create-post", create_post, name="create_post"),
]
