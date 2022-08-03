from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Quick(APIView):
    def get(self, request):
        """Return some string"""
        my_str = 'Construí uma API no Django Rest Framework'
        return Response(my_str)
