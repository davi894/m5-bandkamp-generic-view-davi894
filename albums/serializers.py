from rest_framework import serializers

from .models import Album
import ipdb

# class AlbumSerializernew(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     year = serializers.IntegerField()
#     user_id = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         return Album.objects.create(**validated_data)


class AlbumSerializer(serializers.ModelSerializer):
    def create(self, validated_data):

        return Album.objects.create(**validated_data)

    class Meta:
        model = Album

        fields = [
            "id",
            "name",
            "year",
            "user_id",
        ]

        depth = 1
