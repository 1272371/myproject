from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ServiceOffered(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.name


class ServiceTypes(models.Model):
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
    service_offered = models.ForeignKey(ServiceOffered,
                                        related_name='service_offered',
                                        on_delete=models.CASCADE,)
    requested_by = models.ForeignKey(User, related_name='requested_by',
                                     on_delete=models.CASCADE,)
    brief = models.CharField(max_length=1000, null=True)
