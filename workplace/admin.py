from django.contrib import admin
from .models import Workplace

# from django.db.models import F


# показать все поля
@admin.register(Workplace)
class WorkplaceAdmin(admin.ModelAdmin):
    list_display = [
        "w_worker",
        "w_office",
        "w_level",
        "w_hostname",
        "w_comp",
        "w_printer",
        "w_ip",
        "w_vn",
        "w_display",
        "w_seat_number",
        "w_status",
        "w_inv_number",
        "w_ser_number",
        "w_last_updated",
    ]
    ordering = ["w_level", "w_office", "w_seat_number"]
    search_fields = ["w_hostname", "w_ip", "w_worker"]
    list_filter = ["w_office", "w_level"]
