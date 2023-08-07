
from django.contrib import admin
from django.urls import path,include
from board.views.base_views import index

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include("board.urls")),
    path('users/', include("users.urls")),
    path('blogs/', include("blogs.urls")),
#   http://127.0.0.1:8000/board/
    path("",index,name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
