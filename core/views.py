from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


def index(request):
    return render(request, 'core/index.html')


def exam(request):
    return render(request, 'core/exam.html')


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(methods=['post', 'get'],
                  authentication_classes=[BasicAuthentication],
                  permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        return Response({'enrolled': True})
