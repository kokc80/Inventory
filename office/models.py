from django.db import models


class Office(models.Model):
    office_number = models.CharField(max_length=25, unique=True, verbose_name="Номер кабинета")
    office_name = models.CharField(max_length=100, verbose_name="Название кабинета")
    office_descr =models.CharField(max_length=50, verbose_name="Описание кабинета", null=True, blank=True, default="_")

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"
        ordering = ["office_name",]

    def __str__(self):
        return self.office_name + " - " + self.office_number
