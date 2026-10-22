from django.db import models


# Create your models here.
class Printer(models.Model):
    p_name = models.CharField(max_length=100, verbose_name="Название принтера")
    p_cartridge = models.CharField(max_length=100, verbose_name="Картридж для принтера")

    def __str__(self):
        return f"{self.p_name} ({self.p_cartridge}"

    class Meta:
        verbose_name = "Принтер АРМа"
        verbose_name_plural = "Принтеры АРМа"
        ordering = ("p_name",)


# готов
