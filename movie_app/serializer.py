from rest_framework import serializers
from .models import Director, Movie, Review


def validate_name_min_length(value, min_length):
    if len(value) < min_length:
        raise serializers.ValidationError(f'Имя должно содержать не менее {min_length} символов')
    return value


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, obj):
        return obj.movies.count()

    def validate_text(self, value):
        validate_name_min_length(value, 5)



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_text(self, value):
        validate_name_min_length(value, 5)


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_average_rating(self, obj):
        total_stars = sum(review.stars for review in obj.reviews.all())
        num_reviews = obj.reviews.count()
        if total_stars > 0:
            return total_stars / num_reviews
        else:
            return 0.0

    def validate_title(self, value):
        validate_name_min_length(value, 2)
