from django.urls import path
from . import views

urlpatterns = [
    path("<int:week_num>/", views.home, name="home_past"),
    path('', views.home, name='home'),
    path("workers/", views.workers, name="workers"),
    path("save/", views.save, name="save")
]