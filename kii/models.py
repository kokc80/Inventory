from django.db import models


class Kii(models.Model):
    k_vp_name = models.CharField(max_length=15, unique=True, verbose_name="АП ВипНета")
    k_dl_name = models.CharField(max_length=15, unique=True, verbose_name="Номер DallasLock")
    k_crypto = models.CharField(max_length=15, unique=True, verbose_name="Версия Криптопро")

    class Meta:
        verbose_name = "Данные по КИИ"
        verbose_name_plural = "Данные по КИИ"

    def __str__(self):
        return f"VP - {self.k_vp_name} DL - {self.k_dl_name} Crypto - {self.k_crypto}"
