from django.contrib import admin
from blogging.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

class CategoryInline(admin.TabularInline):
    model = Category

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    model = Post
    fields =['title', 'text', 'author', 'published_date', 'category']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
