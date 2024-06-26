from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('author',)


admin.site.register(Post, PostAdmin)
