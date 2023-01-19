from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer, TemplateHTMLRenderer, \
    StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from mainapp.models import Project, ToDo
from .models import MyUser
from .serializers import MyUserModelSerializer, ProjectHyperlinkedModelSerializer, ToDoModelSerializer

from djangorestframework_camel_case.parser import CamelCaseJSONParser
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.views import APIView


class NoUnderscoreBeforeNumberCamelCaseJSONParser(CamelCaseJSONParser):
    json_underscoreize = {'no_underscore_before_number': True}


class MyUserModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, AdminRenderer, BrowsableAPIRenderer]  # ==> Внутренний Рендер

    queryset = MyUser.objects.all()
    serializer_class = MyUserModelSerializer


class ProjectModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]  # <---<< Внутренний Рендер

    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer


class ToDoModelViewSet(ModelViewSet):
    # parser_classes = (NoUnderscoreBeforeNumberCamelCaseJSONParser,)

    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer


# class ToDoAPIView(APIView):
#
#     def get(self, request, format=None):
#         todo = ToDo.objects.all()
#         serializer = ToDoModelSerializer(todo, many=True)
#         return Response(serializer.data)
#
#     def delete(self, request, pk=None):
#         todo = get_object_or_404(ToDo, pk=pk)
#         serializer = ToDoModelSerializer(todo)
#         return Response(serializer.data)



