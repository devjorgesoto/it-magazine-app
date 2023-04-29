from django.contrib import admin

from .models import Writer, Reader, Article

admin.site.register(Writer)
admin.site.register(Reader)
admin.site.register(Article)
