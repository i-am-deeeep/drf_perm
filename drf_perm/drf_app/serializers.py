from drf_app.models import Movie, Review
from rest_framework import serializers
# from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"

    # user=serializers.StringRelatedField(read_only=True)

    movie_name=serializers.SerializerMethodField()
    user_name=serializers.SerializerMethodField()
    changed_mind=serializers.SerializerMethodField()
    def get_movie_name(self,obj):
        return obj.movie.title
    def get_user_name(self,obj):
        return obj.user.username
    def get_changed_mind(self,obj):
        if obj.created==obj.update:
            return False
        return True
    
    def validate_description(self,value):
        if len(value)>=4:
            return value
        raise serializers.ValidationError("Write a longer description!")

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields="__all__"
    reviews=ReviewSerializer(many=True, read_only=True)
    # reviews=serializers.StringRelatedField(many=True)
    # reviews=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="review-detail")

    # reviews=serializers.SerializerMethodField()
    # def get_reviews(self,obj):
    #     reviews = Review.objects.filter(movie=obj.id)
    #     serializer=ReviewSerializer(reviews, many=True)
    #     return serializer.data

    def validate(self,data):
        if data['title']==data['storyline']:
            raise serializers.ValidationError("Storyline cannot be same as title!")
        return data