from django.contrib import admin
from .models import Post

@admin.register(Post) 
 
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'statut')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'updated_at', 'author')
    readonly_fields = ('created_at', 'updated_at')
# Register your models here.

#
