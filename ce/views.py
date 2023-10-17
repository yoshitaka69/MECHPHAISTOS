from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class SampleAPIView(APIView):

    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)

class IndexView(TemplateView):

    template_name = "index.html"