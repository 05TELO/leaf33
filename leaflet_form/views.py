from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from leaflet_form.utils import save_area_data

from .forms import DynamicForm
from .models import FormData


def dynamic_form_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form_data = request.POST.dict()
        save_area_data(form_data)
    return render(request, "leaflet_form/form.html", {"form": DynamicForm()})


def form_data_list(request: HttpRequest) -> HttpResponse:
    form_data = FormData.objects.all().order_by("-created_at")
    return render(request, "leaflet_form/data_list.html", {"form_data": form_data})
