from encodings import mac_latin2
from tabnanny import verbose

from django.db import models

# Create your models here.
class Office(models.Model):
    office_number = models.CharField(max_length=10, unique=True, verbose_name="Номер кабинета")
    office_level = models.CharField(max_length=2, unique=True, verbose_name="Тип подразделения")
    office_name = models.CharField(max_length=100, verbose_name="Название кабинета")
    office_arm = models.CharField(max_length=20, verbose_name="Название арма в кабинете")
    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"
        ordering = ("id",)
    def __str__(self):
        return self.office_name + " (" + self.office_arm + ")"


class OfficeLevel(models.Model):
    office_level = models.CharField(max_length=2, unique=True, verbose_name="Тип подразделения")
    office_level_name = models.CharField(max_length=20, verbose_name="Наименование подразделения")
    def __str__(self):
        return (self.office_level_name + " (" + self.office_level + ")")
