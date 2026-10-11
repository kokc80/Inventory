from django.contrib import admin
from .models import Workplace


# показать все поля
@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    list_display = ["w_worker", "w_office", "w_level", "w_hostname", "w_comp", "w_printer", "w_ip", "w_display",
                    "w_kii", "w_inv_number", "w_ser_number", "w_seat_number", "w_status", "w_last_updated"]
    search_fields = ["w_worker", "w_hostname"]
