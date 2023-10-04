from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField("Вид", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"

class Owner(models.Model):
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    image = models.ImageField("Изобажение", upload_to="owners/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Хозяин"
        verbose_name_plural = "Хозяины"

class Djaba(models.Model):
    name = models.CharField("Имя", max_length=100)
    image = models.ImageField("Изобажение", upload_to="djabi/")
    category = models.ForeignKey(Category, verbose_name = "Вид", on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Owner, verbose_name="Хозяин", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жаба"
        verbose_name_plural = "Жабы"

    def get_absolute_url(self):
        return reverse('jaba_owner', kwargs = {"pk": self.owner_id, "djaba_name": self.name})
