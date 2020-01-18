from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class HomeView(APIView):

    def get(self, request):
        """
        Return a list of all users.
        """
        return Response({'data': 'Hello world'})
