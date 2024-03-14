from django.contrib import admin
from .models import PriceCard, PriceTable


class PriceCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'pc_description', 'pc_value')
    list_display_links = ('id', 'pc_description')
    list_editable = ('pc_value',)


class PriceTableAdmin(admin.ModelAdmin):
    list_display = ('pt_title', 'pt_old_price', 'pt_new_price')
    list_editable = ('pt_old_price', 'pt_new_price')


admin.site.register(PriceCard, PriceCardAdmin)
admin.site.register(PriceTable, PriceTableAdmin)
