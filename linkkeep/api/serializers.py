from rest_framework import serializers
from linkkeep.api.models import LinkData,LinkCategory



class LinkCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = LinkCategory
		fields = "__all__"


class LinkDataSerializer(serializers.ModelSerializer):
	category = LinkCategorySerializer()
	class Meta:
		model = LinkData
		fields = ["id","title","link","detail","category"]

	def create(self,validated_data):
		category_data = validated_data.pop("category")
		category_instance = LinkCategory.objects.create(**category_data)
		link_data = LinkData.objects.create(**validated_data)
		link_data.category = category_instance
		return link_data