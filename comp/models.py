from django.db import models

# Create your models here.


class Comp(models.Model):
    c_name = models.CharField(max_length=100, verbose_name="Название компьютера")
    c_ddr = models.CharField(max_length=6, verbose_name="Память ДДР XXX Gb")
    c_hdd = models.CharField(max_length=100, verbose_name="Память HDD")
    c_os = models.CharField(max_length=12, verbose_name="Операционная система")
    c_install = models.DateField(null=True, verbose_name="Дата установки")

    def __str__(self):
        return f"{self.c_name} {self.c_pc_ip} {self.c_pc_name}"

    class Meta:
        verbose_name = "Компьютер АРМа"
        verbose_name_plural = "Компьютеры АРМа"
        ordering = ("c_pc_ip", "c_pc_name", "c_name")


# готов
