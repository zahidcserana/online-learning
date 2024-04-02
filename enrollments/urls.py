from django.urls import path
from enrollments import views

urlpatterns = [
    path('enrollments/', views.enrollment_list),
    path('enrollments/<int:pk>/', views.enrollment_detail),
]
