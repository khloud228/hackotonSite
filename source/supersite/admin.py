from django.contrib import admin

from .models import Video, ProcessedVideo, Camera


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'video')
    search_fields = ('id',)


@admin.register(ProcessedVideo)
class ProcessedVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'source_video', 'video')
    search_fields = ('id',)
    raw_id_fields = ('source_video',)


@admin.register(Camera)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id',)
    search_fields = ('id',)
