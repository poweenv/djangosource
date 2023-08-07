
from django.urls import path,include
from .views import post_list,post_edit,post_create,post_delete,post_detail,post_like

app_name="blog"

urlpatterns = [
    # http://127.0.0.1:8000/blogs
    path("",post_list,name="post_list"),
    # http://127.0.0.1:8000/blogs/create/
    path("create/",post_create,name="post_create"),
    path("detail/<int:post_id>/",post_detail,name="post_detail"),
    path("edit/<int:post_id>/",post_edit,name="post_edit"),
    path("delete/<int:post_id>/",post_delete,name="post_delete"),
    # http://127.0.0.1:8000/blogs/likes/1/
    path("like/<int:post_id>/",post_like,name="post_like"),


]
