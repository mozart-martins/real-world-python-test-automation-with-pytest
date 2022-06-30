import pytest
from django.urls import reverse
from typing import List
from companies.models import Company

companies_url = reverse("companies-list")

# Substitui o @pytest.mark.django_db antes de todas as funções
pytestmark = pytest.mark.django_db


@pytest.fixture
def companies(request, company) -> List[Company]:
    companies = []
    names = request.param
    for name in names:
        companies.append(company(name=name))
    return companies


@pytest.fixture
def company(**kwargs):
    def _company_factory(**kwargs) -> Company:
        company_name = kwargs.pop("name", "Test Company Inc")
        return Company.objects.create(name=company_name, **kwargs)
    
    return _company_factory
