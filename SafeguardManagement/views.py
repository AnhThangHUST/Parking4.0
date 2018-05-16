from django.shortcuts import render
from .models import *

# Create your views here.
@api_view(['POST'])
def login(request):
    json = request.data
    try:
        safeguard = Safeguard.objects.get(pk=json["name"])
        if json["password"] != safeguard.getPassword():
            return Response("Wrong Password. You forgot it?", status=status.HTTP_400_BAD_REQUEST)
        return Response()
    except Safeguard.DoesNotExist:
        return Response("No user has that name",status=status.HTTP_404_NOT_FOUND)

