from django.test import TestCase
from courses.serializers import CourseSerializer


class CourseSerializerTest(TestCase):
    def test_serializer_valid_data(self):
        data = {
            "title": "CSE",
            "instructor": "instructor",
            "duration": 555,
            "description": "description",
            "price": 5555
        }
        serializer = CourseSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_data(self):
        data = {
            "title": "",
            "instructor": "instructor",
            "duration": 555,
            "description": "description",
            "price": 5555
        }
        serializer = CourseSerializer(data=data)
        self.assertFalse(serializer.is_valid())
