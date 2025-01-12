from django.contrib import admin

from .models import Category, Location, Post


class PastInline(admin.TabularInline):
    model = Post
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'location',
        'category'
    )
    list_editable = (
        'location',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PastInline,
    )
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PastInline,
    )
    search_fields = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
