from django.contrib import admin
from .models import Article


# Register your models here.
# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ["title", "content", "year", "imgThumb"]
    list_display = ["title", "year"]
    list_filter = ["year"]
    search_fields = ["title", "content"]
