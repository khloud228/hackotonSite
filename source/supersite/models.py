from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.conf import settings
from django.urls import reverse

from source.services import get_path_to_upload


class Video(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='videos',
        verbose_name='Автор'
    )
    video = models.FileField(
        upload_to=get_path_to_upload,
        verbose_name='Файл видео',
        validators=[FileExtensionValidator(allowed_extensions=('mp4',))]
    )


    def __str__(self) -> str:
        return f'Video - {self.id}'


    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class ProcessedVideo(models.Model):
    source_video = models.OneToOneField(
        'Video',
        on_delete=models.CASCADE,
        related_name='processed_video',
        verbose_name='Исходное видео'
    )
    video = models.FileField(
        upload_to=get_path_to_upload,
        verbose_name='Файл обработанного видео',
        validators=[FileExtensionValidator(allowed_extensions=('mp4',))]
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
        upload_to=get_path_to_upload,
        verbose_name='Самый опасный момент',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'png'))]
    )


    def __str__(self) -> str:
        return f'Processed video - {self.id}'
    

    def get_absolute_url(self):
        return reverse('result', kwargs={
            'processed_video_id': self.id
        })


    class Meta:
        verbose_name = 'Обработанное видео'
        verbose_name_plural = 'Обработанное видео'


class Camera(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cameras',
        verbose_name='Автор'
    )
    camera_url = models.CharField(
        max_length=255,
        verbose_name='rtsp ссылка'
    )
    username = models.CharField(
        max_length=55,
        verbose_name='Имя пользователя'
    )
    password = models.CharField(
        max_length=55,
        verbose_name='Пароль'
    )

    def __str__(self):
        return f'{self.id}'
