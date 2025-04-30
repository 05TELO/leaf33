from .models import AreaCollection


def save_area_data(data: dict) -> None:
    areas = []
    i = 1
    while f"name{i}" in data:
        area = {
            "name": data[f"name{i}"],
            "coordinates": {
                "ne_lat": data.get(f"ne_lat{i}"),
                "ne_lng": data.get(f"ne_lng{i}"),
                "sw_lat": data.get(f"sw_lat{i}"),
                "sw_lng": data.get(f"sw_lng{i}"),
            },
        }
        if any(area["coordinates"].values()):
            areas.append(area)
        i += 1
    if areas:
        AreaCollection.objects.create(data=areas)
