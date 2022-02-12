from django.contrib import admin
from.models import list4
class listAdmin4(admin.ModelAdmin):
    list_display = ['img']

# Register your models here.
admin.site.register(list4,listAdmin4)




