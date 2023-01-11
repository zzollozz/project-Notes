from rest_framework.relations import StringRelatedField

from mainapp.models import Project, ToDo
from .models import MyUser
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

class MyUserModelSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email')


class ProjectHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    # users = StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

