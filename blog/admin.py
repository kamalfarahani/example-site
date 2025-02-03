from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "publish", "status"]
    search_fields = ["title", "body"]
    list_filter = ["created", "publish", "author", "status"]
    raw_id_fields = ["author"]
    prepopulated_fields = {"slug": ["title"]}
    date_hierarchy = "publish"
    ordering = ["status", "publish"]
    show_facets = admin.ShowFacets.ALWAYS
