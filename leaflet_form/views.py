from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from leaflet_form.utils import save_area_data

from .forms import DynamicForm
from .models import AreaCollection


def create_area_collection(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form_data = request.POST.dict()
        save_area_data(form_data)
        return redirect("list_area_collections")

    return render(request, "leaflet_form/form.html", {"form": DynamicForm()})


def list_area_collections(request: HttpRequest) -> HttpResponse:
    areas = AreaCollection.objects.all().order_by("-created_at")
    return render(request, "leaflet_form/data_list.html", {"area_collections": areas})
