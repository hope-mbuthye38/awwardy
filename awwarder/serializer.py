from rest_framework import serializers
from .models import Project,Profile
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model =Project
        fields = ('image_path', 'title', 'description')
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profile
        fields = ('profile_image', 'bio')