from django.urls import path
from .views import IndexView, home

urlpatterns = [
    path("", home, name="home"),
    path("index/", IndexView.as_view(), name="index"),
]
