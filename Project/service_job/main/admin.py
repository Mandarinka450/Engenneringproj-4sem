from django.contrib import admin
from .models import Vacancies, Vacancies_cities, Companies, Reviews, Users, Summary, Reviews_about_service
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.contrib import messages
from django.utils.translation import ngettext


class CompaniesInline(admin.TabularInline):
    model = Companies


class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('name_of_vacancy',  'salary_of_mounth', 'graphic_of_work', 'view_summary_link')
    list_filter = ("salary_of_mounth", "graphic_of_work")
    search_fields = ("name_of_vacancy__startswith", )
    inlines = [CompaniesInline]
    actions = ['make_graphic_1', 'make_graphic_2']

    def make_graphic_1(self, request, queryset):
      updated = queryset.update(graphic_of_work='Полная занятость/гибкий график')
      self.message_user(request, ngettext(
            '%d Запись была успешно обновлена',
            '%d Записи были успешно обновлены',
            updated,
        ) % updated, messages.SUCCESS)


    def make_graphic_2(self, request, queryset):
      updated = queryset.update(graphic_of_work='Полная занятость/полный день')
      self.message_user(request, ngettext(
            '%d Запись была успешно обновлена',
            '%d Записи были успешно обновлены',
            updated,
        ) % updated, messages.SUCCESS)


    def view_summary_link(self, obj):
        count = obj.summary_set.count()
        url = (
            reverse("admin:main_summary_changelist")
            + "?"
            + urlencode({"id_vacancies": f"{obj.id_summary}"})
        )
        return format_html('<a href="{}">{} Резюме</a>', url, count)

        view_reviews_link.short_description = "Резюме"



admin.site.register(Vacancies, VacanciesAdmin)




class Vacancies_citiesAdmin(admin.ModelAdmin):
    list_display = ('name_cities', 'quantity_vacancies')
    search_fields = ("name_cities__startswith", )


admin.site.register(Vacancies_cities, Vacancies_citiesAdmin)


class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('name_company', 'description_company', 'rating_company', 'view_reviews_link')
    list_filter = ("rating_company",)
    search_fields = ("name_company__startswith", )


    def view_reviews_link(self, obj):
        count = obj.reviews_set.count()
        url = (
            reverse("admin:main_reviews_changelist")
            + "?"
            + urlencode({"id_company": f"{obj.id_reviews}"})
        )
        return format_html('<a href="{}">{} Отзыв</a>', url, count)

        view_reviews_link.short_description = "Отзыв"


admin.site.register(Companies, CompaniesAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'title', 'message')
    search_fields = ("name__startswith", )


admin.site.register(Reviews, ReviewsAdmin)

class Reviews_about_serviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'title', 'message')
    search_fields = ("name__startswith", )


admin.site.register(Reviews_about_service, Reviews_about_serviceAdmin)



class UsersAdmin(admin.ModelAdmin):
    list_display = ('name_user', 'surname_user', 'email', 'age', 'date_register')
    ordering = ('name_user', 'surname_user')
    actions = ['make_age']

    def make_age(self, request, queryset):
      updated = queryset.update(age='34')
      self.message_user(request, ngettext(
            '%d Запись была успешно обновлена',
            '%d Записи были успешно обновлены',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(Users, UsersAdmin)


class UsersInline(admin.TabularInline):
    model = Users


class SummaryAdmin(admin.ModelAdmin):
    list_display = ('about_myself', 'position_worker', 'work_experience')
    list_filter = ("work_experience", "position_worker")
    search_fields = ("position_worker__startswith", )
    inlines = [UsersInline]


admin.site.register(Summary, SummaryAdmin)




