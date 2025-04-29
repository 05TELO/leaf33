from django.db import transaction

from .models import FormData


def save_area_data(data: dict) -> None:
    coordinates = {
        "ne_lat": data.pop("ne_lat", None),
        "ne_lng": data.pop("ne_lng", None),
        "sw_lat": data.pop("sw_lat", None),
        "sw_lng": data.pop("sw_lng", None),
    }

    with transaction.atomic():
        for key, value in data.items():
            if key.startswith("name"):
                area_data = {"area_name": value, "coordinates": coordinates}
                FormData.objects.create(dynamic_fields=area_data)
