from django.contrib import admin
from us.models import Urls

# Register your models here.

class UrlsAdmin(admin.ModelAdmin):
	list_display = ('short_id', 'long_url', 'pub_date', 'counter')
	ordering = ('-pub_date',)
	
admin.site.register(Urls, UrlsAdmin)