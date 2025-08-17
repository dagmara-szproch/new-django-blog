from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'slug', 'status')
    list_filter = ('status',)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Comment)