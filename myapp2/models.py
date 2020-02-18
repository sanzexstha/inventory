from django.db import models
from django.contrib.auth.models import User

 

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
class Item(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique = True)
    added_date = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    @property
    def get_assigned_employee(self):
        item = Item.objects.get(id=self.id)
 
        s= item.assigned_item.all().first()
        return s



     
 
class ItemRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='item_request')
    item = models.ManyToManyField(Item)

class AssignedItem(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='assigned_employee')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='assigned_item')
    is_active = models.BooleanField(default=True)



