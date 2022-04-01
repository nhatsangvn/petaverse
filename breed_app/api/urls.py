from django.urls import path, include
from breed_app.api.views import BreedsList
from django.views.generic import TemplateView

urlpatterns = [
    path('', BreedsList.as_view(), name='breed-list'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
