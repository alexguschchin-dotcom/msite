from django.db import models
from django.utils import timezone

class Memory(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    text = models.TextField('Текст воспоминания')
    created_date = models.DateTimeField('Дата', default=timezone.now)
    image = models.ImageField('Фотография', upload_to='memories/', blank=True, null=True)

    def __str__(self):
        return self.title

class BabyPhoto(models.Model):
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Фотография', upload_to='baby/')
    description = models.TextField('Описание', blank=True)
    uploaded_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
class OurPhoto(models.Model):
    title = models.CharField('Название', max_length=200)
    image = models.ImageField('Фотография', upload_to='our_photos/')
    description = models.TextField('Описание', blank=True)
    uploaded_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Наше фото'
        verbose_name_plural = 'Наши фото'
