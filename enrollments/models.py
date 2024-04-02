from django.db import models

from courses.models import Course


class Enrollment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    student = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
