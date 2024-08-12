from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    review = models.DecimalField(max_digits=3, decimal_places=1)
    price_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    seats = models.IntegerField()
    transmission = models.CharField(max_length=10, choices=[('AT', 'Automatic'), ('MT', 'Manual')])
    fuel_type = models.CharField(max_length=20)
    year = models.IntegerField()
    gearbox = models.CharField(max_length=10, choices=[('AUTO', 'Automatic'), ('MAN', 'Manual')])
    mileage = models.CharField(max_length=20)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"