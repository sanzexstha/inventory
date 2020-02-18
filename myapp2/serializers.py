from rest_framework import serializers
from .models import  * 
from django.contrib.auth.models import User
 
from rest_framework_jwt.settings import api_settings


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Item
        fields = '__all__'

class ItemRequestSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    item = ItemSerializer( many=True)
    class Meta:
        model = ItemRequest
        fields = '__all__'

class AssignedItemDetailSerializer(serializers.ModelSerializer):
     
    employee = EmployeeSerializer()
    
    class Meta:
        model = AssignedItem
        fields = ('id', 'employee')

class ItemOverviewSerializer(serializers.ModelSerializer):
    assigned_to = AssignedItemDetailSerializer(source = 'get_assigned_employee')
    class Meta:
        model = Item
        fields = '__all__'


 
class GetFullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','is_superuser','is_staff','first_name', 'last_name')


class UserSerializerWithToken(serializers.ModelSerializer):    
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()    

    def get_token(self, object):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER        
        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)        
        return token
    

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = User
        fields = ('token', 'username', 'password', 'first_name',
        'last_name')

 