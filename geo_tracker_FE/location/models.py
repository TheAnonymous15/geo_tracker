from django.db import models

class Location(models.Model):
    device_id = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    location_name = models.CharField(max_length=255, default='')  # Adding a default value to avoid null issue

    class Meta:
        db_table = 'AssetLocation'

    def __str__(self):
        return f"Device {self.device_id} at {self.latitude}, {self.longitude} on {self.timestamp}"
