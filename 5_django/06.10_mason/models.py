from django.db import models 

class Customer(models.Model):
    name = models.CharField(max_lenght=200)
    
    class Meta:
        abstract = True
    
# class Vehicle(models.Model):
#     vehicle_name = models.CharField(max_lenght=200)
#     customer = models.OneToOneField(
#         Customer, on_delete=models.CASCADE, related_name='vehicle'
#   )
    
# one_to_many
class Vehicle(models.Model):
    vehicle_name = models.CharField(max_lenght=200)
    customer = models.Foreing(
        Customer, on_delete=models.CASCADE, related_name='vehicle'
    )
    
    class Meta:
        abstract = True


class Car(Vehicle):
    model_name = models.CharField(max_lenght=200)
    yom= models.DateField()
    

class Worker(models.Model):
    name = models.CharField(max_lenght=200)
    specialty = models.CharField(max_lenght=50)
    

class Machine(models.Model):
    machine_name = models.CharField(max_lenght=200)
    worker = models.ManyToManyField(
        Worker, related_name='machine'
    )
    comm_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['machine_name', '-comm_date']

# do migrations

# shell

Machine.objects.get(id=1).worker.set([ben, michael])
drill.Machine.objects.get(id=2)
drill.worker.set([ben, jo])
drill.worker.all()
drill.worker.all()[:2]

# python manage.py shell
from customers.model import Customer, Vehicle
jessica=Customer.objects.get(id=4)
Vehicle.objects.create(vehicle_name="Toyota Prado", customer=jessica)
Vehicle.objects.create(vehicle_name="Toyota Prado", customer=jessica)

jessica.vehicle.vehicle_name
jessica.vehicle.all()

vehicles = jessica.vehicle.all()
print(vehicles[1:])
vehicles.last()
jessica.vehicle.all().order_by('-id')