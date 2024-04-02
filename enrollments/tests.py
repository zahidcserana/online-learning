from django.test import TestCase
from courses.serializers import CourseSerializer
from enrollments.serializers import EnrollmentSerializer


class EnrollmentSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        data = {
            "title": "CSE",
            "instructor": "instructor",
            "duration": 200,
            "description": "description",
            "price": 5000
        }

        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            course = serializer.data

            enrollmentData = {
                "student": "First student",
                "course_id": course['id']
            }
            serializer = EnrollmentSerializer(data=enrollmentData)
            self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        data = {
            "student": "First student"
        }
        serializer = EnrollmentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
