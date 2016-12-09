from django.contrib import admin

# Register your models here.


from .models import Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price', 'materials', 'height', 'width', 'url')


admin.site.register(Picture, PictureAdmin)
