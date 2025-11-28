from django.contrib import admin

from .models import Student, Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')
    search_fields = ('name', 'surname')
    list_filter = ('name', 'surname')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'age', 'weight', 'height', 'gender',
                    'is_married', 'city', 'created_at')
    search_fields = ('name', 'age', 'city', 'weight')
    list_filter = ('gender', 'is_married')
