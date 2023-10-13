from django.shortcuts import render
from movies.models import RatedMovies
from rest_framework import serializers, status
from movies.serializers import RateMovieSerializer
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
import requests
import json
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny



class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserViewSet, self).get_permissions()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)



class RateMovieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    serializer_class = RateMovieSerializer

    def get_queryset(self):
        user = self.request.user
        return RatedMovies.objects.filter(user=user)

class GetMovies(APIView):

    def get(self, request):
        limit = 10
        page = request.GET.get('page', '0')

        if page.isdigit() and int(page) > 0:
            page = int(page) * 10
        url = f"https://august12-uqf7jaf6ua-ew.a.run.app/movies/?skip={page}&limit={limit}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.content)
        if response.status_code == 200:
            return Response(data, status=status.HTTP_200_OK)
        else:
            response = requests.request("GET", url, headers=headers, data=payload)
            data = json.loads(response.content)
            if response.status_code == 200:
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response(data, status=response.status_code)

