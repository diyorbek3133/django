from rest_framework import serializers
from myapp.models import Lugat


class LugatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lugat
        fields = ['word', 'definition', 'meaning']



    
    




