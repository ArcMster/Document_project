from rest_framework import serializers
from .models import Document

# The following class is for converting python data to JSON and vise versa

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'