from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import serializers
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
            return ItemPostSerializer
        return super().get_serializer_class()
 

class ItemRequestViewSet(viewsets.ModelViewSet):
    queryset = ItemRequest.objects.all()
    serializer_class = ItemRequestViewSerializer
    

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ItemRequestSerializer
 
        return super().get_serializer_class()

  

class RejectRequestViewSet(viewsets.ModelViewSet):
    queryset = RejectedRequest.objects.all()
    serializer_class = RejectedRequestSerializer

    def perform_create(self, serializer):
        item=serializer.validated_data.get('item')
        item.is_accepted = False
        item.save()
        serializer.save()




         

class ItemApproveViewSet(viewsets.ModelViewSet):
    queryset = AssignedItem.objects.all()
    serializer_class = AssignedItemViewSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AssignedItemSerializer
        return super().get_serializer_class()


    def perform_create(self, serializer):
        
        queryset = AssignedItem.objects.filter(
            employee_id=self.request.data.get('employee'),
            item_id=self.request.data.get('item'))
        if queryset.exists():
            raise serializers.ValidationError('already approved')
        item=serializer.validated_data.get('item')
        item.available = False
        item.is_accepted = True
        item.save() 
        serializer.save()

    
    

 



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
