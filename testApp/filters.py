import django_filters
from .models import *

class Setup2Filter(django_filters.FilterSet):
    class Meta:
        model = Setup2
        fields = ['sprache','author']

class AD_Filter(django_filters.FilterSet):
    class Meta:
        model = Setup2
        fields = '__all__'

