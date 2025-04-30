import pytest
from django.test import Client
from django.urls import reverse

from leaflet_form.models import AreaCollection


@pytest.mark.django_db
def test_list_area_collections_empty(client: Client) -> None:
    url = reverse("list_area_collections")
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context["area_collections"]) == 0


@pytest.mark.django_db
def test_list_area_collections_with_data(client: Client) -> None:
    AreaCollection.objects.create(
        data=[
            {
                "name": "Test Area",
                "coordinates": {
                    "ne_lat": "53.9",
                    "ne_lng": "27.5",
                    "sw_lat": "53.8",
                    "sw_lng": "27.4",
                },
            }
        ]
    )

    url = reverse("list_area_collections")
    response = client.get(url)

    assert response.status_code == 200
    assert "area_collections" in response.context

    collections = response.context["area_collections"]
    assert len(collections) == 1
    assert collections[0].data[0]["name"] == "Test Area"
