from django.contrib import admin
from .models import Articles, News
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget



class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Articles, ArticlesAdmin)


class NewsResource(resources.ModelResource):

    class Meta:
        fields = ('id', 'title', 'description',)
        model = News


class NewsAdmin(ImportExportModelAdmin):
    resource_class = NewsResource
    list_display = ('title', 'description')


admin.site.register(News, NewsAdmin)



