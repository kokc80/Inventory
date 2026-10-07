from django.db import models

# Create your models here.


class Workplace(models.Model):
    w_worker = models.CharField(max_length=50, unique=True, verbose_name="Работник АРМа")
    w_level = models.CharField(max_length=5, verbose_name="Уровень АРМа")
    w_comp = models.CharField(max_length=100, verbose_name="Компьютер АРМа")  # spr
    w_printer = models.CharField(max_length=50, verbose_name="Принтер АРМа")  # spr
    w_ip = models.CharField(max_length=5, verbose_name="IP адрес")
    w_name = models.CharField(max_length=5, verbose_name="Название АРМа")
    w_display = models.CharField(max_length=5, verbose_name="Монитор")
    w_cn = models.CharField(max_length=30, verbose_name="Номер кабинета")
    w_on = models.CharField(max_length=5, verbose_name="Отделение")
    w_vn = models.BooleanField(default=False, verbose_name="VipNet")

    def __str__(self):
        return f"{self.w_name} ({self.w_worker})  - {self.w_comp}"
