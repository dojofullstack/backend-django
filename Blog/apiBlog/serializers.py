from rest_framework import serializers
from blogHome.models import *



class ReporterBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = '__all__'



class ArticulosBlogSerializer(serializers.ModelSerializer):
    reporter = ReporterBlogSerializer()

    class Meta:
        model = ArticulosBlog
        # fields = ['id', 'title_blog', 'data_create']
        fields = '__all__'