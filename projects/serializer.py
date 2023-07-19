from rest_framework import serializers
from .models import Project
from technologies.serializer import TechnologySerializer
from libraries.serializer import LibrarySerializer


class ProjectSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Project
        fields = ['id','title', 'created_at', 'repository', 'deploy', 'video', 'cover', 'description', 'highlighted', 'credits', 'content', 'libs', 'technologies' ]
        read_only_fields = ['id', 'created_at']
   

    def to_representation(self, instance):
        if self.context['request'].method == 'GET':
            self.fields['technologies'] = TechnologySerializer(many=True)
            self.fields['libs'] = LibrarySerializer(many=True)
        return super().to_representation(instance)
