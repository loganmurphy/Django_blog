from django.contrib import admin
from blog.models import Publication, Post


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'slug', 'created', 'blog')
    list_filer = ('created')
    search_fields = ('title', 'slug', 'body')

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('category_name',)

class Meta:
  ordering = ['-created']
