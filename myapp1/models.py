from django.db import models
from django.contrib.auth.models import User

 

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
class Item(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique = True)
    added_date = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)
    is_accepted= models.BooleanField(null=True)

    

    @property
    def get_assigned_employee(self):
        item = Item.objects.get(id=self.id)
 
        s= item.assigned_item.all().first()
        return s
   
 
    # @property
    # def is_accepted(self):
    #     if AssignedItem.objects.get(item_id=self.id):
    #         return True
    #     else:
    #         return False
 

class ItemRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='item_request_employee')
    item = models.ManyToManyField(Item, related_name='item_request')

    
class AssignedItem(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assigned_employee')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='assigned_item')
    is_active = models.BooleanField(default=True)

class RejectedRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='rejected_employee')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='rejected_item')
     




