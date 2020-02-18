from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


 
class ItemOverViewViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemOverviewSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ItemSerializer
        return super().get_serializer_class()

class ItemRequestViewSet(viewsets.ModelViewSet):
    queryset = ItemRequest.objects.all()
    serializer_class = ItemRequestSerializer





@api_view(['GET'])
def get_current_user(request):
    
    serializer = GetFullUserSerializer(request.user)
    
    return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self,request):
        user = request.data.get('user')
        if not user:
            return Response({'response' : 'error', 'message' : 'No data found'})
        serializer = UserSerializerWithToken(data = user)

        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({"response" : "error", "message" : serializer.errors})

        return Response({"response" : "success", "message" : "user created succesfully"})
