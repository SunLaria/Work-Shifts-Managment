from django.urls import path
from . import views

urlpatterns = [
    path("<int:week_num>/", views.home, name="home_past"),
    path('', views.home, name='home'),
    path("save/", views.save, name="save"),
    path("delete/",views.delete,name="delete"),
    path("workers/", views.workers, name="workers"),
    path("workers/save/", views.save_worker, name="save_worker"),
    path("workers/remove/<str:worker_id>", views.remove_worker, name="remove_worker")
]