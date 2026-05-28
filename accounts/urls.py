from django.urls import path
from .services import login, logout, refresh

urlpatterns = [
    path("api/auth/login/", login.Login),
    path("api/auth/refresh/", refresh.RefreshAccess),
    path("api/auth/logout/", logout.Logout),
]
