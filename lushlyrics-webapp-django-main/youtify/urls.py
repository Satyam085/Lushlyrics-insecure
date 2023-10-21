from django.contrib import admin
from django.urls import path, include
from userAuth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('login/', views.userLogin, ),
    path('signup/', views.signup),

]
