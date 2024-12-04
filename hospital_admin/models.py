from django.db import models
from shortuuid.django_fields import ShortUUIDField
from base import models as base_model
from doctor import models as doctor_models
from patient import models as patient_models
from Userauthapp import models as Userauthapp_models


class HospitalAdmin(models.Model):
    user = models.OneToOneField(Userauthapp_models.User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.full_name} (Admin)"
class AdminManagement(models.Model):
    service = models.ForeignKey(base_model.Service, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(doctor_models.Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    patient = models.ForeignKey(patient_models.Patient, on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey(base_model.Appointment, on_delete=models.CASCADE, null=True, blank=True)
    billing = models.ForeignKey(base_model.Billing, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Admin Management: {self.service} - {self.doctor} - {self.patient}"

    class Meta:
        ordering = ['-id']


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=500, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    def __str__(self):
        return self.title