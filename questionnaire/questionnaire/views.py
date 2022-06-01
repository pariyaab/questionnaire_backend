import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from questionnaireapp.serializers import ExplanationsSerilizer,ExplanationlistSerilizer,ListSerilizer
from questionnaireapp.models import Explanations,Explanationlist,List
import json
import random


class ExplanationsView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Explanations.objects.all()
        explanation_serializer = ExplanationsSerilizer(qs, many=True)
        return Response(explanation_serializer.data)

class ExplanationlistView(APIView):
    def get(self, request, *args, **kwargs):
        items = list( Explanationlist.objects.all())
        random_items = random.sample(items, 30)
        explanation_list_serilizer = ExplanationlistSerilizer(random_items, many=True)
        explanations_text =[]
        list_text = []
        for item in explanation_list_serilizer.data:
            qs = Explanations.objects.filter(id=item['explnataion'])
            explanation_serializer = ExplanationsSerilizer(qs, many=True)
            explanations_text.append(explanation_serializer.data)
            qs = List.objects.filter(id=item['list'])
            list_serializer = ListSerilizer(qs,many=True)
            list_text.append(list_serializer.data)

        json_explanations = json.dumps(explanations_text, indent=4, default=str)
        print(json_explanations)
        print("================================")
        json_list = json.dumps(list_text, indent=4, default=str)
        print(json_list)
        return Response({
            'explanations': explanations_text,
            'lists': list_text
            })
