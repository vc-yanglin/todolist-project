from django.urls import path
from .views import user_register, user_login

# from . import views as xxx
# xxx.user_register

urlpatterns = [
    path("register/", user_register, name="register"),
    path("login/", user_login, name="login"),
]
