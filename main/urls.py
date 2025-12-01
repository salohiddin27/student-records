from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import StudentModelViewSet, TeacherModelViewSet

router = DefaultRouter()
router.register('all_students', StudentModelViewSet, basename='student')
router.register('teacher', TeacherModelViewSet , basename='teacher')

urlpatterns = (
    path('', include(router.urls)),
)
