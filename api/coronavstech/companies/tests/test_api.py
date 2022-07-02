import django

# django.setup()
import json
import pytest
from django.urls import reverse

from typing import List

from companies.models import Company

companies_url = reverse("companies-list")

# Substitui o @pytest.mark.django_db antes de todas as funções
pytestmark = pytest.mark.django_db

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> GET <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


@pytest.fixture
def amazon() -> Company:
    return Company.objects.create(name="Amazon")


def test_one_company_exists_should_succeed(client, amazon) -> None:
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == amazon.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> POST <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def test_create_company_without_arguments_should_fail(client) -> None:
    response = client.post(path=companies_url)
    assert response.status_code, 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_existing_company_should_fail(client) -> None:
    test_company = Company.objects.create(name="Apple")
    response = client.post(path=companies_url, data={"name": "Apple"})
    assert response.status_code, 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }


def test_create_company_with_only_name_should_create(client) -> None:
    response = client.post(path=companies_url, data={"name": "Another company"})
    assert response.status_code, 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "Another company"
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_layoffs_status_should_succeed(client) -> None:
    response = client.post(
        path=companies_url, data={"name": "Another company 2", "status": "Layoffs"}
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"


def test_create_company_with_wrong_status_should_fail(client) -> None:
    response = client.post(
        path=companies_url, data={"name": "Another company 2", "status": "WrongStatus"}
    )
    assert response.status_code == 400
    assert "WrongStatus" in str(response.content)
    assert "is not a valid choice" in str(response.content)


@pytest.mark.xfail
def test_should_be_ok_if_fails(client) -> None:
    assert 1 == 2


@pytest.mark.skip
def test_should_skip(client) -> None:
    assert 1 == 2


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> LEARNING ABOUT FIXTURE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# All fixtures are in conftest.py file.


@pytest.mark.parametrize(
    "companies",
    [["TikTok", "Twich", "Test Company Inc"], ["Facebook", "Instagram"]],
    ids=["3 T Companies", "Zuckerberg's Companies"],
    indirect=True,
)
def test_multiple_companies_exists_should_succeed(client, companies) -> None:
    company_names = set(map(lambda x: x.name, companies))
    print(company_names)
    response_companies = client.get(companies_url).json()
    assert len(company_names) == len(response_companies)
