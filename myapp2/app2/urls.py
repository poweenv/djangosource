from .views import index
from django.urls import path

# 앱의 네임스페이스 지정
app_name= "app2"


urlpatterns = [
    path("",index, name="detail"),
]
