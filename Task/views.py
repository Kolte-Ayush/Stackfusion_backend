from django.shortcuts import render
from .models import UserForm
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .service.EmailService import EmailService
from .service.EmailMessage import EmailMessage
from .service.EmailBuilder import EmailBuilder


# Create your views here.
class UserCreation(APIView):
    @staticmethod
    def get(request):
        user_form = UserForm.objects.all()
        serialize_form = UserSerializer(user_form, many=True)
        return Response(serialize_form.data)

    @staticmethod
    def post(request):
        serialize_form = UserSerializer(data=request.data)
        if serialize_form.is_valid():
            emsg = EmailMessage()
            emsg.to = [request.data['email']]
            emsg.subject = "Registration"
            mailrespone = EmailService.send(emsg)
            if mailrespone == 1:
                serialize_form.save()
                return Response(serialize_form.data, status=status.HTTP_201_CREATED)
        return Response(serialize_form.errors, status=status.HTTP_400_BAD_REQUEST)
