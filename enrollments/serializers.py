from rest_framework import serializers
from courses.models import Course
from courses.serializers import CourseSerializer
from enrollments.models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'created', 'student', 'course', 'course_id']
