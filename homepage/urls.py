from django.urls import path, reverse
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("secondPage/", SecondPage.as_view(), name="sp"),
    path("tree/", TreePage.as_view(), name="tr"),
]