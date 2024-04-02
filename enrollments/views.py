from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from enrollments.models import Enrollment
from enrollments.serializers import EnrollmentSerializer


@csrf_exempt
def enrollment_list(request):
    """
    List all code enrollments, or create a new enrollment.
    """
    if request.method == 'GET':
        enrollments = Enrollment.objects.all()
        student = request.GET.get('student')

        if student is not None:
            enrollments = enrollments.filter(student__icontains=student)

        serializer = EnrollmentSerializer(enrollments, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EnrollmentSerializer(data=data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def enrollment_detail(request, pk):
    """
    Retrieve, update or delete a code enrollment.
    """
    try:
        enrollment = Enrollment.objects.get(pk=pk)
    except Enrollment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EnrollmentSerializer(enrollment)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EnrollmentSerializer(enrollment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        enrollment.delete()
        return HttpResponse(status=204)
