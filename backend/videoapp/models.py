from django.db import models

from .validators import validate_file_extension


class CreatedUpdated(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Filter(CreatedUpdated):
    '''
    Add filter title to fetch filters from frontend.
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Video(CreatedUpdated):
    '''
        Model to add videos.
    '''
    title = models.CharField(max_length=255)
    video_file = models.FileField(
        upload_to='videos/', validators=[validate_file_extension])
    processed_video = models.FileField(
        upload_to='processed_videos/', null=True, blank=True)
    thumbnail = models.FileField(
        upload_to='thumbnails/', null=True, blank=True)

    def __str__(self):
        return self.title


class Language(models.Model):
    '''
        Model to add languages for different subtitles.
    '''
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubtitleFiles(CreatedUpdated):
    '''
        Model to add subtitle files.
    '''
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name='video_subtitles')
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name='language')

    subtitle = models.FileField(
        upload_to='subtitles/', validators=[validate_file_extension])

    def __str__(self):
        return self.video.title


class Filtered_Videos(models.Model):
    '''
        Model to add filter added video files.
    '''
    filtered_video = models.FileField(upload_to='modified_videos/')
    applied_filter = models.ForeignKey(
        Filter, on_delete=models.CASCADE, related_name="filter_apply")
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name="filter_video")

    class Meta:
        unique_together = ["applied_filter", "video"]

    def __str__(self):
        return f'filter- {self.applied_filter.name}, title- {self.video.title}'
