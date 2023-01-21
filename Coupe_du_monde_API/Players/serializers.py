from rest_framework import serializers
from Players.models import Players

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:

        model =  Players
        fields = ['id', 'name', 'goals']
