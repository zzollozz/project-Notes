from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, AdminRenderer, TemplateHTMLRenderer, \
    StaticHTMLRenderer
from rest_framework.viewsets import ModelViewSet

from mainapp.models import Project, ToDo
from .models import MyUser
from .serializers import MyUserModelSerializer, ProjectHyperlinkedModelSerializer, ToDoModelSerializer

from djangorestframework_camel_case.parser import CamelCaseJSONParser
from rest_framework.generics import CreateAPIView


class NoUnderscoreBeforeNumberCamelCaseJSONParser(CamelCaseJSONParser):
    json_underscoreize = {'no_underscore_before_number': True}


class MyUserModelViewSet(ModelViewSet):
    renderer_classes = [AdminRenderer, BrowsableAPIRenderer]  # ==> Внутренний Рендер

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



