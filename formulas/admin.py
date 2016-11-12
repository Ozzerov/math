from django.contrib import admin

# Register your models here.

from .models import Formula


class FormulaAdmin(admin.ModelAdmin):
    list_display = ('order', 'subject', 'theme', 'formula', 'comment')


admin.site.register(Formula, FormulaAdmin)
