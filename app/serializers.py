from rest_framework import serializers
from app.models import KRMap,\
    Connection


class KRMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = KRMap
        fields = (
            'identifier',
            'workitem_ids'
        )


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = (
            'name',
            'email',
            'meta_data'
        )
