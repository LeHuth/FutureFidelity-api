from rest_framework import serializers
from music.models import Vinyl, Track
from products.serializers import RatingModelSerializer

class TrackSerializer(serializers.ModelSerializer):
    """
    TrackSerializer is a ModelSerializer for the Track model.
    It is used to serialize Track objects into a format that can be easily rendered into JSON, XML, or other content types.
    It includes all fields in the Track model.
    """

    class Meta:
        model = Track
        fields = '__all__'


class VinylListSerializer(serializers.ModelSerializer):
    """
    VinylListSerializer is a ModelSerializer for the Vinyl model.
    It is used to serialize Vinyl objects into a format that can be easily rendered into JSON, XML, or other content types.
    It includes all fields in the Vinyl model.
    """

    class Meta:
        model = Vinyl
        fields = ['id', 'name', 'price', 'image']


class VinylDetailSerializer(serializers.ModelSerializer):
    """
    VinylDetailSerializer is a ModelSerializer for the Vinyl model. It is used to serialize a single Vinyl object
    into a format that can be easily rendered into JSON, XML, or other content types. It includes all fields in the
    Vinyl model and also adds the artist's name, artist's id, genre's name, genre's id, label's name, label's id,
    category's name, and category's id to the serialized data.
    """

    track_list = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = Vinyl

        fields = '__all__'

    def get_track_list(self, obj):
        """
        get_track_list is a method that returns a serialized list of tracks associated with the Vinyl instance.

        Parameters:
        obj (Vinyl): A Vinyl instance.

        Returns:
        list: A list of serialized Track instances associated with the Vinyl instance.
        """
        return TrackSerializer(obj.tracks.all(), many=True).data

    def get_ratings(self, obj):
        """
        get_ratings is a method that returns a serialized list of ratings associated with the Vinyl instance.

        Parameters:
        obj (Vinyl): A Vinyl instance.

        Returns:
        list: A list of serialized Rating instances associated with the Vinyl instance.
        """
        return RatingModelSerializer(obj.ratings.all(), many=True).data

    def to_representation(self, instance):
        """
        to_representation method is used to convert the Vinyl instance into a dictionary that can be rendered into
        JSON, XML, or other content types. It calls the parent class's to_representation method and then adds the
        artist's name, artist's id, genre's name, genre's id, label's name, label's id, category's name,
        and category's id to the returned dictionary.

        Parameters:
        instance (Vinyl): A Vinyl instance.

        Returns:
        dict: A dictionary representation of the Vinyl instance.
        """
        representation = super().to_representation(instance)

        representation['artist'] = dict(name=instance.artist.name, id=instance.artist.id)

        representation['genre'] = dict(name=instance.genre.name, id=instance.genre.id)

        representation['label'] = dict(name=instance.label.name, id=instance.label.id)

        representation['category'] = dict(name=instance.category.name, id=instance.category.id)

        return representation
