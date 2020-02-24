from django.urls import path

from .views import redirect_view, ShortenURL

urlpatterns = [
    path('createshort/', ShortenURL.as_view()),
    path('<slug:tiny>/', view=redirect_view, name='short_url_view')

]
