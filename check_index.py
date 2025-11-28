import os
import django

# Django settings faylini sozlash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
django.setup()

from main.models import Student
from django.db import connection

# ORM query
qs = Student.objects.filter(name="Salohiddin")

# SQL va parametrlarni ajratib olish
sql, params = qs.query.sql_with_params()

print("Generated SQL query:")
print(sql)
print("Params:", params)

# Explain query plan
with connection.cursor() as cursor:
    cursor.execute("EXPLAIN QUERY PLAN " + sql, params)
    explain_result = cursor.fetchall()

print("\nEXPLAIN QUERY PLAN result:")
for row in explain_result:
    print(row)
