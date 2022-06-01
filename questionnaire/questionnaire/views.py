import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from questionnaireapp.serializers import ExplanationsSerilizer
from questionnaireapp.models import Explanations
class TestView(APIView):
    def get(self, request, *args, **kwaargs):
        data = {
            "username":"pariya joon",
            "year_enrolled" : 15
        }
        return Response(data)

class ExplanationsView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Explanations.objects.all()
        game_serializer = ExplanationsSerilizer(qs, many=True)
        return Response(game_serializer.data)
