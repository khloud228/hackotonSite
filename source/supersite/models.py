from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Video(models.Model):
#     title = models.CharField(
#         max_length=255,
#         verbose_name='Название',
#         default='Без названия',
#         blank=True,
#         null=True
#     )
    video = models.FileField(
        # upload_to=''
        verbose_name='Файл видео'
    )


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class ProcessedVideo(models.Model):
    video = models.FileField(
        verbose_name='Файл обработанного видео'
    )
    threat_degree = models.FloatField(
        default=0.0,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(1.0)
        ],
        verbose_name='Степень угрозы'
    )
    AI_VERDICTS = (
        ('Безопасно', 'безопасно'),
        ('Подозрительно', 'подозрительно'),
        ('Опасно', 'опасно')
    )
    ai_verdict = models.CharField(
        max_length=25,
        choices=AI_VERDICTS,
        default='Безопасно',
        verbose_name='Вердикт искуственного интелекта.'
    )
    most_dangerous = models.ImageField(
        verbose_name='Самый опасный момент',
        blank=True,
        null=True
    )


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Обработанное видео'
        verbose_name_plural = 'Обработанное видео'