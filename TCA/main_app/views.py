from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main_app.Serializer import *
from main_app.models import *


class SliderPicApi(viewsets.ModelViewSet):
    serializer_class = SliderSer
    queryset = SliderPic.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]





class NewsApi(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AgentsApi(viewsets.ModelViewSet):
    serializer_class = AgentsSerial
    queryset = Agents.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ImagesApi(viewsets.ModelViewSet):
    serializer_class = ImagesSerial
    queryset = Images.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TableApi(viewsets.ModelViewSet):
    serializer_class = TableSerial
    queryset = Table.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PermiTableApi(viewsets.ModelViewSet):
    serializer_class = PermiTableSerial
    queryset = PermiTable.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostApi(viewsets.ModelViewSet):
    serializer_class = PostSerial
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#
# @api_view(['GET'])
# def SliderPicget(request):
#     mod = SliderPic.objects.all()
#     serializer = SliderSer(mod, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def SliderPicDetail(request, pk):
#     mod = SliderPic.objects.filter(id=pk)
#     if mod:
#         serializer = SliderSer(mod, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({'error': 'Maglumat tapylmady'})
#
#
# @api_view(['GET'])
# def NewsGet(request):
#     if request.method == 'GET':
#         mod = News.objects.all()
#         serializer = NewsSerializer(mod, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def NewsApiDetail(request, pk):
#     mod = News.objects.filter(id=pk)
#     if mod:
#         serializer = NewsSerializer(mod, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({'error': 'Maglumat tapylmady'})
#
#
# @api_view(['GET'])
# def AgentsGet(request):
#     if request.method == 'GET':
#         mod = Agents.objects.all()
#         serializer = AgentsSerial(mod, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def AgentsApiDetail(request, pk):
#     mod = Agents.objects.filter(id=pk)
#     if mod:
#         serializer = AgentsSerial(mod, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({'error': 'Maglumat tapylmady'})
#
#
# @api_view(['GET'])
# def ImagesGet(request):
#     if request.method == 'GET':
#         mod = Images.objects.all()
#         serializer = ImagesSerial(mod, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def ImagesApiDetail(request, pk):
#     mod = Images.objects.filter(id=pk)
#     if mod:
#         serializer = ImagesSerial(mod, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({'error': 'Maglumat tapylmady'})
#
#
# @api_view(['GET'])
# def TablesGet(request):
#     if request.method == 'GET':
#         mod = Table.objects.all()
#         serializer = TableSerial(mod, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET'])
# def TablesApiDetail(request, pk):
#     mod = Table.objects.filter(id=pk)
#     if mod:
#         serializer = TableSerial(mod, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({'error': 'Maglumat tapylmady'})
#
#
# @api_view(['GET'])
# def PermiTableGet(request):
#     mod = PermiTable.objects.all()
#     serializer = PermiTableSerial(mod, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def PermiTableApiDetail(request, pk):
#     mod = PermiTable.objects.filter(id=pk)
#     if mod:
#         serializer = PermiTableSerial(mod, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({'error': 'Maglumat tapylmady'})
#
#
# @api_view(['GET'])
# def PostGet(request):
#     mod = Post.objects.all()
#     serializer = PostSerial(mod, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def PostDetail(request, pk):
#     mod = Post.objects.filter(id=pk)
#     if mod:
#         serializer = PostSerial(mod, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({'error': 'Maglumat tapylmady'})
