from django.db.models import Count, Sum, F, Value
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Student, Teacher
from .serializers import StudentSerializers, TeacherSerializers, TeacherWithSerializers


class TeacherModelViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
    filter_backends = [DjangoFilterBackend]

    @action(detail=True, methods=['get'])
    def with_students(self, request, pk=None):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = StudentSerializers(teacher.students.all(), many=True)
        return Response(serializer.data)


class TeacherWithViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherWithSerializers
    filter_backends = [DjangoFilterBackend]

    @action(detail=True, methods=['get'])
    def with_students(self, request, pk=None):
        teacher = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherWithSerializers(teacher)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def fullname(self, request):
        data = Teacher.objects.values('name', 'surname').annotate(
            fullname=Concat(F('name'), Value(' '), F('surname'))
        )
        return Response(list(data))

    @action(detail=False, methods=['get'])
    def teacher_student_count(self, request):
        data = Teacher.objects.annotate(total_students=Count('students'))
        result = [
            {"teacher": t.name, "students": t.total_students}
            for t in data
        ]
        return Response(result)


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['teacher']

    @action(detail=False, methods=['get'])
    def distinct_city(self, request):
        data = Student.objects.values('city').distinct()
        return Response(list(data))

    @action(detail=False, methods=['get'])
    def count_name(self, request):
        count = Student.objects.values('name').distinct().count()
        return Response({"total_unique_names": count})

    @action(detail=False, methods=['get'])
    def count_surname(self, request):
        count = Student.objects.values('surname').distinct().count()
        return Response({"total_unique_surnames": count})

    @action(detail=False, methods=['get'])
    def order_by_name(self, request):
        data = Student.objects.values('name').annotate(
            count=Count('name')
        ).order_by('name')
        return Response(list(data))

    @action(detail=False, methods=['get'])
    def order_by_age(self, request):
        data = Student.objects.values('name', 'age').order_by('age')
        return Response(list(data))

    @action(detail=False, methods=['get'])
    def sum_age(self, request):
        total = Student.objects.aggregate(total_age=Sum('age'))
        return Response(total)

    @action(detail=False, methods=['get'])
    def group_by(self, request):
        data = Student.objects.values('surname').annotate(
            total=Count('surname')
        )
        return Response(list(data))

    @action(detail=False, methods=['get'])
    def fullname(self, request):
        data = Student.objects.values('name', 'surname').annotate(
            fullname=Concat(F('name'), Value(' '), F('surname'))
        )
        return Response(list(data))
