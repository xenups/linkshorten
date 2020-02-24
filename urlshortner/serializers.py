from rest_framework import serializers

from urlshortner import models


class PhoneValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Urls
        fields = ('urls', 'shorten_url')
