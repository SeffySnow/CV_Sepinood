from django.contrib import admin
from home.models import Message


# admin.site.register(Message)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    search_fields = ("title",'name','email')
    list_display = ('email',"title",'name')
