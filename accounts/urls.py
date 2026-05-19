from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    path('login/', views.login),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),

    path('google-login/', views.google_login),
    path('google-callback/', views.google_callback),
]