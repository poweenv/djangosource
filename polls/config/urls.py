from django.contrib import admin
from django.urls import path, include
from polls.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path("", index),
]
