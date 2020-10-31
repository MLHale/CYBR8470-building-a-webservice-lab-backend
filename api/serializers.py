from rest_framework import serializers
from models import Breed, Dog


class BreedSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    size = serializers.CharField(required=False, allow_blank=True, max_length=100)
    friendliness = serializers.IntegerField(read_only=True)
    trainability = serializers.IntegerField(read_only=True)
    sheddingamount = serializers.IntegerField(read_only=True)
    exerciseneeds = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Breed` instance, given the validated data.
        """
        return Breed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Breed` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
        instance.trainability = validated_data.get('trainability', instance.trainability)
        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
        instance.save()
        return instance
