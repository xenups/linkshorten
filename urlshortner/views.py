from django.shortcuts import render

from django.apps import apps
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.response import Response

from urlshortner import models
from urlshortner.util import encode, decode


def redirect_view(request, tiny):
    try:
        url_id = decode(tiny)
    except ValueError:
        raise Http404('Bad encoded ID.')

    url = get_object_or_404(models.Urls, pk=url_id).url
    return redirect('http://' + url)


class ShortenURL(generics.GenericAPIView):
    @staticmethod
    def post(request, *args, **kwargs):
        url = str(request.data['url']).strip()
        url = models.Urls.objects.create(url=url)
        url.save()
        shorten_url = encode(url.id)
        models.Urls.objects.filter(url=url).update(shorten_url=shorten_url)
        shorten_url = '127.0.0.1/' + shorten_url
        return Response(({shorten_url}), status=status.HTTP_200_OK)
