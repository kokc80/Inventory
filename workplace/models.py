from django.db import models
from comp.models import Comp
from office.models import Office
from printer.models import Printer


class Workplace(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "В работе"
        MAINTENANCE = "maintenance", "На обслуживании"
        DECOMMISSIONED = "decommissioned", "Списан"
        RESERVED = "reserved", "Зарезервирован"

    class Level(models.IntegerChoices):
        LEVEL_0 = 0, "АХЧ"
        LEVEL_1 = 1, "ПОЛИКЛИНИКА"
        LEVEL_2 = 2, "CТАЦИОНАР"
        LEVEL_3 = 3, "ПРОЧИЕ"
        LEVEL_4 = 4, "ПТД"
        LEVEL_6 = 5, "ВА"
        LEVEL_5 = 6, "ФАП"

    w_worker = models.CharField(max_length=50, unique=True, verbose_name="Работник АРМа")
    w_office = models.ForeignKey(Office, null=True, on_delete=models.SET_NULL, related_name="offices_workplaces")
    w_level = models.IntegerField(choices=Level.choices, default=Level.LEVEL_0, verbose_name="Уровень АРМа")
    w_hostname = models.CharField(max_length=10, default="WRK", verbose_name="ХОСТ АРМа")
    w_comp = models.ForeignKey(Comp, null=True, on_delete=models.SET_NULL, related_name="comps_workplaces")
    w_printer = models.ForeignKey(
        Printer, null=True, on_delete=models.SET_NULL, related_name="printers_workplaces", blank=True
    )
    w_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP адрес", default="10.81.58.1")
    w_vn = models.CharField(max_length=20, default=" ", verbose_name="ВипНет АП")
    w_display = models.CharField(blank=True, max_length=50, verbose_name="Монитор")
    w_os = models.CharField(max_length=20, default="Windows 10", verbose_name="Операционная система")
    w_install = models.DateField(null=True, verbose_name="Дата установки")
    w_inv_number = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="Инв. номер")
    w_ser_number = models.CharField(max_length=50, null=True, blank=True, verbose_name="Серийный номер")
    w_seat_number = models.CharField(max_length=10, null=True, blank=True, verbose_name="Номер места/стола")
    w_status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE, verbose_name="Статус")
    w_last_updated = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

    def __str__(self):
        return f"{self.w_hostname} ({self.w_worker})  - {self.w_comp}"

    class Meta:
        verbose_name = "АРМ"
        verbose_name_plural = "АРМы"
        ordering = ["w_level", "w_office", "w_seat_number"]
