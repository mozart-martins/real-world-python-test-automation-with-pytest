from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .serializers import CompanySerializer
from .models import Company


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination


@api_view(http_method_names = ['POST'])
def send_company_email(request: Request) -> Response:
    """_summary_
        sends email with request payload
        sender: mozart.dias.martins@gmail.com
        receiver: mozart.dias.martins@gmail.com
        
        POST
        {
            "subject": "Meu assunto legal",
            "message": "Seja bem-vindo ao meu mundo"
        }
    """
    send_mail(
        request.data.get("subject"),
        request.data.get("message"),
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    
    return Response({"status": "success", "info": "email sent successfully"}, status = 200)