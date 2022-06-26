from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from fibonacci.naive import fibonacci_naive

from .serializers import CompanySerializer
from .models import Company


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
    

class FibonacciException(Exception):
    def __str__(self):
        return "Number must be an int and a natural number."


class FibonacciView(APIView):
    def get(self, request: Request):
        n = request.query_params.get("n")
        if n is None:
            return Response("Hello there, no number was passed", status=200)
        try:
            n = int(n)
        except ValueError:
            raise FibonacciException()
        if n < 0:
            raise FibonacciException()

        fibonacci_result = fibonacci_naive(n)
        return Response({"number": n, "result": fibonacci_result}, status=200)


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
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email='from@example.com',
        recipient_list=['to@example.com'],
        fail_silently=False,
    )
    
    return Response({"status": "success", "info": "email sent successfully"}, status = 200)