from django.urls import path

from .services import login, logout, me, refresh
from .services import register

urlpatterns = [
    path("api/auth/login/", login.Login),
    path("api/auth/register/", register.Register),
    path("api/auth/refresh/", refresh.RefreshAccess),
    path("api/auth/logout/", logout.Logout),
    path("api/auth/me/", me.me),
]
