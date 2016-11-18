from django.contrib import admin

# Register your models here.

from .models import Subject, Theme, Formula


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('order', 'subject', 'description')


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('order', 'subject', 'theme')


class FormulaAdmin(admin.ModelAdmin):
    list_display = ('order', 'theme', 'header', 'formula', 'image')
    list_filter = (
        ('theme', admin.RelatedOnlyFieldListFilter),
    )


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Formula, FormulaAdmin)
