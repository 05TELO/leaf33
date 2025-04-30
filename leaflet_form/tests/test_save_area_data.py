import pytest

from leaflet_form.models import AreaCollection
from leaflet_form.views import save_area_data


@pytest.mark.django_db
def test_save_area_data_success():
    test_data = {
        "name1": "Test Area 1",
        "ne_lat1": "53.9",
        "ne_lng1": "27.5",
        "sw_lat1": "53.8",
        "sw_lng1": "27.4",
        "name2": "Test Area 2",
        "ne_lat2": "54.9",
        "ne_lng2": "28.5",
        "sw_lat2": "54.8",
        "sw_lng2": "28.4",
    }

    save_area_data(test_data)

    collection = AreaCollection.objects.first()
    assert collection is not None
    assert len(collection.data) == 2
    assert collection.data[0]["name"] == "Test Area 1"
    assert collection.data[1]["coordinates"]["ne_lat"] == "54.9"
