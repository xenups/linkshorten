from rest_framework import serializers

from urlshortner import models


class URLSerializer(serializers.ModelSerializer):
    url = serializers.CharField(required=True)

    class Meta:
        model = models.Urls
        fields = ('url',)
