from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="store"),
    re_path(r'^\d+', views.detail, name="detail"),
    # re_path(r'^electronics', views.electronics, name="electronics"),
    re_path(r'^electronics', views.electronics, name="electronics"),
]
