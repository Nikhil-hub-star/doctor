from django.db import models

# Create your models here.
class Home(models.Model):

    doctor_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(upload_to="home/")

    experience_years = models.IntegerField()
    surgeries = models.IntegerField()
    consultations = models.IntegerField()
    awards = models.IntegerField()

    def __str__(self):
        return self.doctor_name