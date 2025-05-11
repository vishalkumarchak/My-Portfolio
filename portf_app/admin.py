from django.contrib import admin
from .models import Project, Message

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'created_at')  
    search_fields = ('title', 'technologies')  
    list_filter = ('created_at',)  

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')  
    search_fields = ('name', 'email', 'subject')  
    list_filter = ('sent_at',)  

admin.site.register(Project, ProjectAdmin)
admin.site.register(Message, MessageAdmin)