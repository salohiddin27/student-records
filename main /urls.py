from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import StudentModelViewSet, TeacherModelViewSet, TeacherWithViewSet

router = DefaultRouter()
router.register('all_students', StudentModelViewSet, basename='student')
router.register('teacher', TeacherModelViewSet , basename='teacher')
# router.register('teacher_with_students', TeacherWithViewSet, basename='teacher_with_students')

urlpatterns = (
    path('', include(router.urls)),
)
