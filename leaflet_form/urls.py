from django.urls import path

from . import views

urlpatterns = [
    path("", views.dynamic_form_view, name="dynamic_form"),
    path("data/", views.form_data_list, name="form_data_list"),
]
