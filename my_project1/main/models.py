from django.db import models


class mac(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("описание товара")
    photo = models.FileField(upload_to="img", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "маки"
        verbose_name_plural = "мак"


class iphone(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("описание товара")
    photo = models.FileField(upload_to="img", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "айфоны"
        verbose_name_plural = "айфон"


class ipad(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("описание товара")
    photo = models.FileField(upload_to="img", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "айпады"
        verbose_name_plural = "айпад"


class watch(models.Model):
    title = models.CharField("Название", max_length=50)
    description = models.TextField("описание товара")
    photo = models.FileField(upload_to="img", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "часики"
        verbose_name_plural = "часы"


class airpods(models.Model):
    title = models.CharField("Название", max_length=50)
    content = models.TextField("описание товара", blank=True)
    photo = models.FileField(upload_to="img", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "наушники"
        verbose_name_plural = "наушник"
