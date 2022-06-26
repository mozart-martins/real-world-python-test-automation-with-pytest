from django.contrib import admin
from django.urls import path, include

from companies.urls import companies_router
from companies.views import send_company_email, FibonacciView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(companies_router.urls)),
    path("send-email", send_company_email),
    path('fibonacci', FibonacciView.as_view(), name='fib-seq'),
]
