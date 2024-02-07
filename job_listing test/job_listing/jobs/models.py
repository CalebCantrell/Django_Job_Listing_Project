from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.TextField()
    requirements = models.TextField()
    app_deadline = models.DateTimeField()

    def __str__(self):
        return self.title