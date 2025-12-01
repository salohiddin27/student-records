from django.db import models
from django.db.models import CASCADE


class Teacher(models.Model):
    name = models.CharField(max_length=222, db_index=True)
    surname = models.CharField(max_length=222)
    information = models.CharField(max_length=20, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'surname'], name='names_index'),
        ]

    def __str__(self):
        return f"{self.name} {self.surname}"


class Student(models.Model):
    name = models.CharField(max_length=222)
    surname = models.CharField(max_length=222)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    gender = models.CharField(max_length=6)
    is_married = models.BooleanField()
    city = models.CharField(max_length=222)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=CASCADE, related_name='students')

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['surname']),
            models.Index(fields=['city']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return (
            f"{self.name} {self.surname}, Age: {self.age}, "
            f"Weight: {self.weight}, Height: {self.height}, "
            f"Gender: {self.gender}, Married: {self.is_married}, "
            f"City: {self.city}"
        )
