# comp\models.py
from django.db import models


class Comp(models.Model):
    c_name = models.CharField(max_length=25, verbose_name="Название компьютера")
    c_ddr = models.CharField(max_length=6, verbose_name="Память ДДР XXX Gb")
    c_hdd = models.CharField(max_length=6, verbose_name="Память HDD")
    c_descr = models.CharField(max_length=50, verbose_name="Описание", null=True, blank=True, default="_")

    def __str__(self):
        return f"{self.c_name} {self.c_ddr} {self.c_hdd} "

    class Meta:
        verbose_name = "Компьютер АРМа"
        verbose_name_plural = "Компьютеры АРМа"
        ordering = (
            "c_name",
        )


# готов
