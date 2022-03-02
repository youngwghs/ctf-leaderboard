from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib.auth import views as auth_views #import this
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("challenges/", views.challenges, name="challenges"),
    path("submit", views.submit, name="submit"),
    path("board", views.board, name="board"),
    path("rules", views.rules, name="rules"),

    #path('accounts/profile/', profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    #path('accounts/', include('django.contrib.auth.urls')), # new
    path('logout', LogoutView.as_view(), name='logout'),

]
