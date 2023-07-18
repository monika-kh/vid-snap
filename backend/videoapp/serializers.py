from rest_framework import serializers
from .models import Video, SubtitleFiles, Language, Filter


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class SubtitleFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtitleFiles
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['language_name'] = instance.language.name
        return representation


class VideoSerializer(serializers.ModelSerializer):
    subtitles = SubtitleFilesSerializer(many=True, read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


class FiltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'
