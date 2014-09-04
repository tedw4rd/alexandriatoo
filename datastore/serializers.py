from datastore.models import MetadataCategory, MetadataValue, Tag
from datastore.models import ArtifactCategory, Artifact, Build
from rest_framework import serializers


class MetadataCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MetadataCategory
		read_only_fields = ('slug', 'friendly_name', 'required', 'values')


class MetadataValueSerializer(serializers.HyperlinkedModelSerializer):
	category = MetadataCategorySerializer()
	class Meta:
		model = MetadataValue
		read_only_fields = ('value', 'builds')


class TagSeralizer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tag
		read_only_fields = ('value', 'builds')


class ArtifactCategorySeralizer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ArtifactType
		read_only_fields = ('slug', 'friendly_name', 'extension')


class ArtifactSeralizer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Artifact
		fields = ('a_type', 'build')


class BuildSerializer(serializers.HyperlinkedModelSerializer):
	tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='value')	
	class Meta:
		model = Build
		


