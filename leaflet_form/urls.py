from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_area_collection, name="create_area_collection"),
    path("areas/", views.list_area_collections, name="list_area_collections"),
]
