from django.urls import path
from . import views
# 앱의 네임스페이스 지정
app_name= "users"


urlpatterns = [
    path("", views.user_main, name="main"),
    path("register/", views.signup, name="register"),
    path("login/", views.common_login, name="login"),
    path("logout/", views.common_logout, name="logout"),
]
