import pytest
from django.test import Client
from django.urls import reverse
from pytest_mock import MockerFixture


@pytest.mark.django_db
def test_create_area_collection_get(client: Client) -> None:
    url = reverse("create_area_collection")
    response = client.get(url)

    assert response.status_code == 200
    assert "form" in response.context


@pytest.mark.django_db
def test_create_area_collection_post_success(
    client: Client, mocker: MockerFixture
) -> None:
    url = reverse("create_area_collection")
    mock_save = mocker.patch("leaflet_form.views.save_area_data")

    response = client.post(
        url,
        {
            "name1": "Test Area",
            "ne_lat1": "53.9",
            "ne_lng1": "27.5",
            "sw_lat1": "53.8",
            "sw_lng1": "27.4",
            "csrfmiddlewaretoken": "dummy_token",
        },
    )

    assert response.status_code == 302
    assert response.url == reverse("list_area_collections")
    mock_save.assert_called_once()
