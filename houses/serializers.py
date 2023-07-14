from rest_framework import serializers
from houses.models import Houses, Land, Agent, Client

class HousesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = '__all__'
        
class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = '__all__'        
        
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'
        
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
# User Register and Login


        
                       