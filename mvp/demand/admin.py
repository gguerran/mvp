from django.contrib import admin
from django.utils.html import mark_safe

from mvp.demand.models import Demand
from mvp.settings import STATIC_URL


class DemandAdmin(admin.ModelAdmin):
    list_display = [
        'description', 'state', 'city', 'email', 'phone', 'status_',
        'advertiser', 'created_at',
    ]

    def status_(self, obj):
        if obj.status == 'Finalizada':
            return mark_safe(
                "<img src='" + STATIC_URL +
                "/img/baseline-check_circle_outline.svg' alt='Aberta'>"
            )
        if obj.status == 'Aberta':
            return mark_safe(
                "<img src='" + STATIC_URL +
                "/img/baseline-highlight_off.svg' alt='Aberta'>"
            )
    
    status_.__name__ = 'status de finalização'


admin.site.register(Demand, DemandAdmin)