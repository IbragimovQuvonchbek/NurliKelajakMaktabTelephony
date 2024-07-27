from django.db import models


class Call(models.Model):
    phone_number = models.CharField("Номер телефона", max_length=20, blank=False)
    full_name = models.CharField("Имя", max_length=255, blank=True)
    description = models.TextField("Описание", blank=False)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Запись вызова"
        verbose_name_plural = "Записи вызовов"
