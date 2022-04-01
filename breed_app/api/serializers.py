from rest_framework import serializers
from breed_app.models import Breed

class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = "__all__"
        #fields = ['id', 'name', 'description']
        #exclude = ['active']

