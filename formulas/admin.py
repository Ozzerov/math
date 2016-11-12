from django.contrib import admin

# Register your models here.

from .models import Theme, Formula


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('order', 'subject', 'theme')


class FormulaAdmin(admin.ModelAdmin):
    list_display = ('order', 'subject', 'theme', 'formula', 'comment')


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Formula, FormulaAdmin)
