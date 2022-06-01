from django.db.models.fields import files
from rest_framework import fields, serializers
from .models import Explanations

class ExplanationsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Explanations
        fields = ('id','text','tweet_id')