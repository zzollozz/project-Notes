from .models import MyUser
from rest_framework.serializers import ModelSerializer

class MyUserModelSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('username', 'first_name', 'last_name', 'email')
