from django.urls import path
from django.urls import path, include
from .views import (
    VideoListCreateView,
    SubtitleListCreateView,
    VideoRetrieveUpdateDestroyView,
    LanguageListView,
    ApplyFilterUpdateView,
    FilterListView
)

urlpatterns = [
    path("videos/", VideoListCreateView.as_view(), name="video_upload"),
    path(
        "videos/<int:pk>/",
        VideoRetrieveUpdateDestroyView.as_view(),
        name="video-detail",
    ),
    path("subtitles/", SubtitleListCreateView.as_view(), name="subtitles"),
    path("languages", LanguageListView.as_view(), name="language"),
    path("add-filer/<int:pk>/", ApplyFilterUpdateView.as_view(), name="edit-video"),
    path("filters", FilterListView.as_view(), name="filters"),
    
    
    

]
