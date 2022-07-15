from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.detail, name="detail"),
    path("rooms", views.allRooms, name="allRooms"),
    path("new", views.new, name="new")
]
