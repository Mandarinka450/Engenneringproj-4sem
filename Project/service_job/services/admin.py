from django.contrib import admin
from .models import Services, Specialist
from django.contrib import messages
from django.utils.translation import ngettext


class SpecialistInline(admin.TabularInline):
    model = Specialist


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'tariff_plan', 'price')
    search_fields = ("price__startswith", )
    inlines = [SpecialistInline]
    actions = ['make_price_2300']


    def make_price_2300(self, request, queryset):
      updated = queryset.update(price='2300')
      self.message_user(request, ngettext(
            '%d Запись была успешно обновлена',
            '%d Записи были успешно обновлены',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(Services, ServicesAdmin)


class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'description')
    search_fields = ("name__startswith", )


admin.site.register(Specialist, SpecialistAdmin)


