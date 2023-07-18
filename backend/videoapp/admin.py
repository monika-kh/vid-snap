from django.contrib import admin
from .models import Video, SubtitleFiles, Language, Filter, Filtered_Videos


admin.site.register(Video)
admin.site.register(SubtitleFiles)
admin.site.register(Language)
admin.site.register(Filter)
admin.site.register(Filtered_Videos)
