from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from courses.models import Course
from courses.serializers import CourseSerializer


@csrf_exempt
def course_list(request):
    """
    List all code courses, or create a new course.
    """
    if request.method == 'GET':
        courses = Course.objects.all()
        title = request.GET.get('title')
        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        duration_from = request.GET.get('duration_from')
        duration_to = request.GET.get('duration_to')

        if title is not None:
            courses = courses.filter(title__icontains=title)
        if price_from is not None and price_to is not None:
            courses = courses.filter(price__range=(price_from, price_to))
        if duration_from is not None and duration_to is not None:
            courses = courses.filter(duration__gte=duration_from, duration__lte=duration_to)

        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def course_detail(request, pk):
    """
    Retrieve, update or delete a code course.
    """
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(course, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        course.delete()
        return HttpResponse(status=204)
