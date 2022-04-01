from django.urls import path, include
from breed_app.api.views import BreedsList

urlpatterns = [
    path('', BreedsList.as_view(), name='breed-list'),
]
