from django.urls import path
from utilisateurs.views import acceuil, user_login, user_logout, register,about,start

urlpatterns = [
    path('', acceuil, name="home"),
    path('', start, name="index"),
    path('about', about, name="about"),
    path('register', register, name="register"),
    path('login', user_login, name="login"),
    path('logout', user_logout, name="logout"),
]