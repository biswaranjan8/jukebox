from rest_framework import serializers
from .models import Musicians, Music_Albums


class MusiciansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musicians
        fields = "__all__"


class Music_AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music_Albums
        fields = "__all__"



class MusiciansUpdateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Musicians
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.musician_type(validated_data.get('musician_type', instance.musician_type))
        instance.save()
        return instance


class Music_AlbumsUpdateSerialier(serializers.ModelSerializer):
    class Meta:
        model = Music_Albums
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.musician = validated_data.get('musician', instance.musician)
        instance.album_name = validated_data.get('album_name', instance.album_name)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
