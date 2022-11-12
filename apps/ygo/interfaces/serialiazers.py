from rest_framework import serializers 

class DeckSerializer(serializers.Serializer):
    """Serializer definition for Deck."""
    name = serializers.CharField()
    player_id = serializers.IntegerField()
    main_deck = serializers.IntegerField()
    extra_deck = serializers.IntegerField()
    side_deck = serializers.IntegerField()
    cards = serializers.ListField() 

class GBPlayerSerializer(serializers.Serializer):
    player = serializers.IntegerField()
    amount = serializers.IntegerField()
    
class GBArchetypeSerializer(serializers.Serializer):
    archetype = serializers.CharField()
    amount = serializers.IntegerField()
    
class PlaceSerializer(serializers.Serializer):
    municipe = serializers.CharField()
    province = serializers.CharField()
    
    


