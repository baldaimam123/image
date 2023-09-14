from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = [
        "slug",
        "update",
        "publish",
    ]


admin.site.register(Post, PostAdmin)
