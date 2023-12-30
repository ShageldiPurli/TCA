from rest_framework import serializers

from main_app.models import *


class SliderSer(serializers.ModelSerializer):
    class Meta:
        model = SliderPic
        fields = '__all__'


class AgentsSerial(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class ImagesSerial(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class TableSerial(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class PermiTableSerial(serializers.ModelSerializer):
    class Meta:
        model = PermiTable
        fields = '__all__'


class PostSerial(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
