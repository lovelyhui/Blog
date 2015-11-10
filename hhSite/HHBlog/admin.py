from django.contrib import admin
from .models import Author, Tag, Classification, Article


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('caption', 'classification', 'publish_time')
    list_filter = ['publish_time']
    search_fields = ['caption']

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Classification)
admin.site.register(Article, ArticleAdmin)
