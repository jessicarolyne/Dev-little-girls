from django.contrib import admin
from site_devlittlegirls_app.models import Site

class SiteAdmin(admin.ModelAdmin):
    exclude = ['data']
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Site)
