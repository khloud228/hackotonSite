from django.db import models


class Video(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название',
        default='Без названия',
        blank=True,
        null=True
    )
    video = models.FileField(
        # upload_to=''
        verbose_name='Файл видео'
    )


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
