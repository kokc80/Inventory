from django.db import models


class Office(models.Model):
    office_number = models.CharField(max_length=10, unique=True, verbose_name="Номер кабинета")
    office_name = models.CharField(max_length=100, verbose_name="Название кабинета")
    office_arm = models.CharField(max_length=20, verbose_name="Название арма в кабинете")

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"
        ordering = ("office_number",)

    def __str__(self):
        return self.office_name + " (" + self.office_arm + ")"
