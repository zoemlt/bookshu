from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("space/<str:pk>", views.space, name="space"),
]
