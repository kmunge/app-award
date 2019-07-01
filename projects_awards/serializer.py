from rest_framework import serializers
from .models import Profile, Projects

class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('bio','user','email')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=('title','description','url','date')