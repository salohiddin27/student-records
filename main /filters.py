import django_filters

from .models import Student, Teacher


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'name': ['icontains', 'startswith', 'endswith'],
            'surname': ['icontains', 'startswith', 'endswith']
        }


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'name': ['icontains', 'startswith', 'endswith'],
            'surname': ['icontains', 'startswith', 'endswith'],
            'age': ['gte', 'lte', 'lt', 'gt'],
            'weight': ['gte', 'lte', 'lt', 'gt'],
            'gender': ['icontains', 'startswith', 'endswith'],
            'city': ['icontains', 'startswith', 'endswith'],
        }
