from django.shortcuts import render
from rest_framework import status, viewsets
from linkkeep.api.models import LinkData
from linkkeep.api.serializers import LinkDataSerializer
# Create your views here.



class LinkDataReadCreate(viewsets.ModelViewSet):
	queryset = LinkData.objects.all()
	serializer_class = LinkDataSerializer

	def get_queryset(self):
		queryset = self.queryset
		user = self.request.user
		return queryset.filter(user=user)
