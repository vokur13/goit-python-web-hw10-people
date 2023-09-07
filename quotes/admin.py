from django.contrib import admin

from .models import Author, Tag, Quote


# admin.site.register(Author)
# admin.site.register(Tag)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("fullname", "born_date", "born_location", "biography")
    prepopulated_fields = {"slug": ("fullname",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ("tag",)
    prepopulated_fields = {"slug": ("tag",)}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Quote)
