from rest_framework import generics
from .utils import apply_filters, merge_clips
from .models import Video, SubtitleFiles, Language, Filter
from .serializers import (
    FiltersSerializer,
    VideoSerializer,
    SubtitleFilesSerializer,
    LanguageSerializer,
)
from rest_framework.response import Response


class LanguageListView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        data = response.data
        for item in data:
            video_id = item["id"]
            subtitles = self.queryset.get(id=video_id).video_subtitles.all()
            subtitle_data = SubtitleFilesSerializer(subtitles, many=True).data
            item["subtitles"] = subtitle_data
        return response


class VideoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get(self, *args, **kwargs):
        video = Video.objects.get(id=kwargs["pk"])
        subtitle_file = SubtitleFiles.objects.filter(
            video=kwargs["pk"], language=self.request.query_params["lang"]
        )
        if subtitle_file:
            merge_clip = merge_clips(video, subtitle_file[0])
            serializer = VideoSerializer(merge_clip)
            return Response(serializer.data)
        return Response({"message": "File Not Found"})


class SubtitleListCreateView(generics.ListCreateAPIView):
    queryset = SubtitleFiles.objects.all()
    serializer_class = SubtitleFilesSerializer


class ApplyFilterUpdateView(generics.RetrieveUpdateAPIView):
    def patch(self, request, pk):
        video = Video.objects.get(id=pk)
        filter = Filter.objects.get(id=self.request.query_params["filter"])
        filtered_video = apply_filters(video, filter)
        return Response(filtered_video.headers["Content-Disposition"])


class FilterListView(generics.ListCreateAPIView):
    queryset = Filter.objects.all()
    serializer_class = FiltersSerializer
