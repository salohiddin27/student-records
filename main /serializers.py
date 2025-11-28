from rest_framework import serializers

from .models import Student, Teacher


class StudentSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y, %H:%M:%S")
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'surname', 'full_name', 'age', 'weight',
                  'height', 'gender', 'is_married', 'city',
                  'created_at'
                  ]

    def get_full_name(self, obj):
        return f"{obj.name} {obj.surname}"


class TeacherSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'surname', 'full_name', 'information']

    def get_full_name(self, obj):
        return f"{obj.name} {obj.surname}"


class TeacherWithSerializers(serializers.ModelSerializer):
    students = StudentSerializers(many=True, read_only=True)
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'full_name', 'information', 'students']

    def get_full_name(self, obj):
        return f"{obj.name} {obj.surname}"
