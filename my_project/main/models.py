from django.db import models


class mac(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "маки"
        verbose_name_plural = "мак"


class iphone(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "айфоны"
        verbose_name_plural = "айфон"


class ipad(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "айпады"
        verbose_name_plural = "айпад"


class watch(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True)
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "часики"
        verbose_name_plural = "часы"


class airpods(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "наушники"
        verbose_name_plural = "наушник"


class main_card(models.Model):
    title = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена товара", null=True, )
    photo = models.FileField(upload_to="img", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "главные страницы"
        verbose_name_plural = "главная страница"


class menuwatch(models.Model):
    title = models.CharField("Название", max_length=50)
    content = models.TextField("описание", null=True, max_length=256)
    size = models.CharField("размер", null=True, blank=True, max_length=20, )
    imgcolor2 = models.ImageField(upload_to="img", null=True)
    imgcolor3 = models.ImageField(upload_to="img", null=True)
    imgcolor4 = models.ImageField(upload_to="img", null=True)
    imgcolor5 = models.ImageField(upload_to="img", null=True)
    imgcolor6 = models.ImageField(upload_to="img", null=True)
    imgcolor7 = models.ImageField(upload_to="img", null=True)
    imgcolor8 = models.ImageField(upload_to="img", null=True)
    imgcolor9 = models.ImageField(upload_to="img", null=True)
    imgcolor10 = models.ImageField(upload_to="img", null=True)
    list = models.TextField("Описание продукта", null=True, max_length=5706)
    photowatch = models.ImageField("фото часов", upload_to="img", null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "меню"
        verbose_name_plural = "меню часов"

class iphonemenu(models.Model):
    title = models.CharField("Название", max_length=50)
    content = models.TextField("описание", null=True, max_length=256)
    imgcolor2 = models.ImageField(upload_to="img", null=True)
    imgcolor3 = models.ImageField(upload_to="img", null=True)
    imgcolor4 = models.ImageField(upload_to="img", null=True)
    imgcolor5 = models.ImageField(upload_to="img", null=True)
    size = models.CharField("Емкость", null=True, blank=True, max_length=20, )
    size2 = models.CharField("Емкость2", null=True, blank=True, max_length=20, )
    size3 = models.CharField("Емкость3", null=True, blank=True, max_length=20, )
    size4 = models.CharField("Емкость4", null=True, blank=True, max_length=20, )
    sim = models.CharField("SIM", null=True, blank=True, max_length=20, )
    sim2 = models.CharField("SIM2", null=True, blank=True, max_length=20, )
    sim3 = models.CharField("SIM3", null=True, blank=True, max_length=20, )
    list = models.TextField("Описание продукта", null=True, max_length=2706)
    photoiphone = models.ImageField("фото Айфона",upload_to="img", null=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mеню"
        verbose_name_plural = "меню айфонов"
