from django.db import models


class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100, blank=True, default='')
    duration = models.IntegerField()
    description = models.TextField(null=True)
    price = models.FloatField()

    class Meta:
        ordering = ['created']
