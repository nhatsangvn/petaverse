from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from breed_app.models import Breed
from breed_app.api.serializers import BreedSerializer

class BreedsList(APIView):

    def post(self, request):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ### Nhan's Code
            content = {
              "msg" : "Implementing"
            }
            return Response(content, status=500)
        else:
            return Response(serializer.errors)
