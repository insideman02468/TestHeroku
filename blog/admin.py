from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class Entry(admin.ModelAdmin):
    pass
