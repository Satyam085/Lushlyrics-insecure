from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.default, name='default'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page'),
    path("accounts/login/", views.userLogin, name='login'),
    path("logout", views.signout, name = 'signout'),
    path('signup', views.signup, name='signup')
]