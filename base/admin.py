from django.contrib import admin
from .models import Announcement, Contact, IstekOneri, Person


@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('name_surname', 'job', 'gender', 'create_time', 'tcno',)
    list_filter = ('name_surname', 'gender',)
    search_fields = ('name_surname', 'job')


admin.site.register(Contact)
admin.site.register(Announcement)
admin.site.register(IstekOneri)

# Register your models here.
