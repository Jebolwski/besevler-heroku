from cgitb import lookup
from dataclasses import field
import django_filters
from django_filters import CharFilter
from django import forms
from .models import Person

class PersonFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name_surname",lookup_expr="icontains",widget=forms.TextInput(attrs={'placeholder': 'Ad Soyad','class':'name'}))
    job = CharFilter(field_name="job",lookup_expr="icontains",widget=forms.TextInput(attrs={'placeholder': 'İş','class':'job'}))
    tcno = CharFilter(field_name="tcno",lookup_expr="icontains",widget=forms.TextInput(attrs={'placeholder': 'TC No','class':'tcno'}))
    class Meta:
        model = Person
        fields = ["gender"]
        exclude=['user','create_time']
