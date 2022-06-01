
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from questionnaireapp.serializers import ExplanationsSerilizer,ExplanationlistSerilizer,ListSerilizer,UserSerilizer,ExplanationusersSerilizer
from questionnaireapp.models import Explanations,Explanationlist,List,Users
import json
import random
import jwt

def checkToken(token):
      qs = Users.objects.filter(token=token)
      user = UserSerilizer(qs, many=True)
      if len(user.data) > 0:
          return True
      return False

class ExplanationsView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Explanations.objects.all()
        explanation_serializer = ExplanationsSerilizer(qs, many=True)
        return Response(explanation_serializer.data)

class ExplanationlistView(APIView):
    def get(self, request, *args, **kwargs):
        token = request.META['HTTP_AUTHORIZATION'].split('Bearer')[1].strip()
        if(checkToken(token)):
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
        else:
            return Response({'error': 'you dont have permission'})

class SignUpUsers(APIView):

    def post(self, request, *args, **kwargs):
        payload = {
            'first_name': request.data['first_name'],
            'last_name': request.data['last_name'],
        }

        jwt_token = {'token': jwt.encode(payload, "SECRET_KEY", algorithm='HS256')}
        print(jwt_token)
        request.data._mutable = True
        request.data['token'] = jwt_token['token']

        serializer = UserSerilizer(data=request.data)

        if serializer.is_valid():
            selectedObject = serializer.save()
            selectedObject.save()
            return Response(jwt_token)

        return Response(serializer.errors)

class AddExplanationsAnswer(APIView):
    def post(self, request, *args, **kwargs):
        token = request.META['HTTP_AUTHORIZATION'].split('Bearer')[1].strip()
        if(checkToken(token)):
            request.data._mutable = True
            qs = Users.objects.filter(token=token)
            user = UserSerilizer(qs, many=True)
            request.data['user_id'] = user.data['id']
            serializer = ExplanationusersSerilizer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
        else:
            return Response({'error': 'you dont have permission'})
            