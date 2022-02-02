
# to make sure we can edit the data through the admin panel, we have to register them

from django.contrib import admin

from .models import Post, Author, Tag

# Register your models here


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)   # tuples ; we add some filter
    list_display = ("title", "date", "author",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)