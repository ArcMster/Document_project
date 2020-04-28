from documentapi.viewsets import DocumentViewset
from rest_framework import routers

#This file is for configuring the routing of applications
#All the requests in the format host/api will be handled by this file

router = routers.DefaultRouter()
router.register('document',DocumentViewset)