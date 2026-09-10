from django.contrib import admin
from .models import articles
# Register your models here.
@admin.register(articles)
class articlesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','status')
    
    