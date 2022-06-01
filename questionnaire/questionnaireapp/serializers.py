from django.db.models.fields import files
from rest_framework import fields, serializers
from .models import Explanations,Explanationlist,List

class ExplanationsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Explanations
        fields = ('id','text','tweet_id')


class ExplanationlistSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Explanationlist
        fields = ('id','explnataion','list','rank')

class ListSerilizer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('id','list_id','list_name')