import requests
import json
import pytest
from faker import Faker
from companies.models import Company

testing_env_companies_env = "http://127.0.0.1:8000/companies/"

# Substitui o @pytest.mark.django_db antes de todas as funções
pytestmark = pytest.mark.django_db


def test_zero_companies_django_agnostic() -> None:
    response = requests.get(url=testing_env_companies_env)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_create_company_with_layoffs_django_agostic() -> None:
    response = requests.post(
        url=testing_env_companies_env,
        json={"name": Faker().name(), "status": "Layoffs"},
    )

    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("status") == "Layoffs"

    cleanup_company(company_id=str(response_content["id"]))


def cleanup_company(company_id: str) -> None:
    response = requests.delete(url=testing_env_companies_env + company_id)
    assert response.status_code == 204


@pytest.mark.poke
def test_pokeapi() -> None:
    response = requests.get(
        url="https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
    )
    response_content = json.loads(response.content)

    assert response.status_code == 200
    assert response_content["results"][0]["name"] == "bulbasaur"


# this package that is able to mock response. You should look for the documentation
import responses
@pytest.mark.poke
@responses.activate
def test_mocked_pokeapi() -> None:
    # this code mocks the api response
    responses.add(
        method=responses.GET,
        url="https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0",
        json={"results": [{"name": "pikachu"}]},
        status=200,
    )

    assert process_pokeapi() == 25
    
    
def process_pokeapi() -> None:
    response = requests.get(
        url="https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
    )
    response_content = json.loads(response.content)

    if response.status_code != 200:
        raise ValueError("Request para a Pokeapi mockada FALHOU!")
        
    pokemon_name = response_content["results"][0]["name"]

    if pokemon_name == "pikachu":
        # Yay! A resposta esta mockada 
        return 25
    
    return 42