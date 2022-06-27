from django.contrib import admin

# Register your models here.
from demoapp.models import shop,background,traditional,kerala

admin.site.register(shop)
admin.site.register(background)
admin.site.register(traditional)
admin.site.register(kerala)