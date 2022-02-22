from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.submit, name="submit"),
    path("board", views.board, name="board"),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('logout', LogoutView.as_view()),

]
