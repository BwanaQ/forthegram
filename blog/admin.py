from django.contrib import admin

# Register your models here.
from .models import Image, Comment


class CommentInline(admin.StackedInline):
    model = Comment


class ImageAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)
