from django.db import models


class Office(models.Model):
    office_number = models.CharField(max_length=25, unique=True, verbose_name="Номер кабинета")
    office_name = models.CharField(max_length=100, verbose_name="Название кабинета")

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"
        ordering = ("office_number",)

    def __str__(self):
        return " №" + self.office_number + " " + self.office_name
