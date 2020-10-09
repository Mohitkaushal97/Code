from django.shortcuts import render

# Create your views here.
import time

from data.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
 
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import FormM
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Create your views here.

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        

        return super(LoginAPI, self).post(request, format=None)

@login_required(login_url='api/login/')
def subscribe(request):
    sub = forms.Subscribe()


    if request.method == 'POST':
        

        sub = forms.Subscribe(request.POST)



        recepient= request.POST.get('email')
        subject= request.POST.get('subject')


        message= request.POST.get('message')


        send_mail(subject, 
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)



        return render(request, 'index.html')
    return render(request, 'elements.html', {'form':sub})





            