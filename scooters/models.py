from django.db import models
from django.conf import settings
from django.utils import timezone

class Scooter(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=50, unique=True)
    is_available = models.BooleanField(default=True)
    battery_level = models.PositiveIntegerField(default=100)  # battery % for example
    image = models.ImageField(upload_to='scooters/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'Available' if self.is_available else 'Rented'})"


class Ride(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rides')
    scooter = models.ForeignKey(Scooter, on_delete=models.CASCADE, related_name='rides')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def duration(self):
        if self.end_time:
            delta = self.end_time - self.start_time
            return delta.total_seconds() / 60  # duration in minutes
        return None

    def calculate_cost(self):
        if self.end_time:
            # ₹30 per minute
            minutes = self.duration()
            return round(minutes * 30, 2)
        return 0

    def save(self, *args, **kwargs):
        if self.end_time and (self.cost is None):
            self.cost = self.calculate_cost()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ride by {self.user.username} on {self.scooter.identifier} started at {self.start_time}"