from django.db import models
from django.db.models import URLField
from django.utils.timezone import now


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs", "Layoffs"
        HIRING_FREEZE = "Hiring Freeze", "Hiring Freeze"
        HIRING = "Hiring", "Hiring"

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20, choices=CompanyStatus.choices, default=CompanyStatus.HIRING,
    )
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = URLField(blank=True)
    notes = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"
