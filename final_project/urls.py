from django.contrib import admin
from django.urls import path

from board.views import index
from user.views import LoginView, RegisterView, logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("logout/", logout),
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
]
