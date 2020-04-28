from rest_framework import viewsets
from . import models
from . import serializers

# The below class will create internal funcions like list(), retrive(), create(), destroy() etc. for various web methods like GET, POST, PUT and DELETE etc.
class DocumentViewset(viewsets.ModelViewSet):
    queryset = models.Document.objects.all()
    #the above code will assign all the objects in Document table to the variable: queryset
    serializer_class = serializers.DocumentSerializer
    # The above serializer_class initialization will use DocumentSerializer for JSON conversion for DocumentViewset