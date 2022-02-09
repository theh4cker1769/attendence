from tracemalloc import start
import django_filters
from django_filters import DateFilter
from . models import *

class StudentFilter(django_filters.FilterSet):
    date = DateFilter(field_name='date', lookup_expr='time')
    class Meta:
        model = Student
        fields = ['ien', 'branch', 'attendence']
