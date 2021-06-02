from django.contrib import admin
from hello.models import Topic, Entry, Class, Blog

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Class)
admin.site.register(Blog)

