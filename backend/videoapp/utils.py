import os
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import pysrt
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx import all as vfx
from .models import Video, Filtered_Videos


def time_to_seconds(time_obj):
    return (
        time_obj.hours * 3600
        + time_obj.minutes * 60
        + time_obj.seconds
        + time_obj.milliseconds / 1000
    )


def create_subtitle_clips(
    subtitles, videosize, fontsize=24, font="Arial", color="yellow", debug=False
):
    """
    Function to merge video clip and the subtitles.
    """
    subtitle_clips = []

    for subtitle in subtitles:
        start_time = time_to_seconds(subtitle.start)
        end_time = time_to_seconds(subtitle.end)
        duration = end_time - start_time

        video_width, video_height = videosize

        text_clip = (
            TextClip(
                subtitle.text,
                fontsize=fontsize,
                font=font,
                color=color,
                bg_color="black",
                size=(video_width * 3 / 4, None),
                method="caption",
            )
            .set_start(start_time)
            .set_duration(duration)
        )
        subtitle_x_position = "center"
        subtitle_y_position = video_height * 4 / 5

        text_position = (subtitle_x_position, subtitle_y_position)
        subtitle_clips.append(text_clip.set_position(text_position))

    return subtitle_clips


def merge_clips(video, subtitle_file):
    """
    Function to store the processed video in the database.
    """
    video = Video.objects.get(id=video.id)

    video_clip = VideoFileClip("videoproject/" + video.video_file.url)
    subtitles = pysrt.open("videoproject/" + subtitle_file.subtitle.url)

    begin, end = ("videoproject/" + video.video_file.url).split(".mp4")

    output_video_file = begin + "_subtitled" + ".mp4"

    print("Output file name: ", output_video_file)
    # Create subtitle clips
    subtitle_clips = create_subtitle_clips(subtitles, video_clip.size)

    final_video = CompositeVideoClip([video_clip] + subtitle_clips)
    final_video.write_videofile(output_video_file, codec="libx264", audio_codec="aac")

    # Get processed video file path and store it in the table.
    cleaned_path = os.path.normpath(output_video_file)
    path_parts = cleaned_path.split(os.path.sep)
    file_name = path_parts[-1]

    if video.processed_video._file is not None:
        os.remove(video.processed_video.path)

    video.processed_video = "videos/" + file_name
    video.save()
    return video


def apply_filters(video, filter):
    if video.processed_video:
        url = video.processed_video.url
    elif video.video_file:
        url = video.video_file.url

    clip = VideoFileClip("videoproject" + url)

    if filter.name == "blackwhite":
        clip = clip.fx(vfx.blackwhite)
    elif filter.name == "invert_colors":
        clip = clip.fx(vfx.invert_colors)
    elif filter.name == "fadein":
        clip = clip.fx(vfx.fadein, duration=2)

    begin, end = ("videoproject/" + video.video_file.url).split(".mp4")
    output_file_path = begin + "_modeified." + "mp4"

    filtered_clip = clip
    filtered_clip = filtered_clip.set_audio(clip.audio)

    filtered_clip.write_videofile(output_file_path, codec="libx264", audio_codec="aac")

    clip.close()

    cleaned_path = os.path.normpath(output_file_path)
    path_parts = cleaned_path.split(os.path.sep)
    file_name = path_parts[-1]

    path = "videos/" + file_name
    try:
        filtered_objects = Filtered_Videos.objects.create(
            video=video, applied_filter=filter, filtered_video=path
        )
    except:
        filtered_objects = Filtered_Videos.objects.filter(
            video=video, applied_filter=filter
        )[0]

    # Open the modified video file
    download_file = download(filtered_objects, output_file_path)
    return download_file


def download(filtered_objects, output_file_path):
    video_file = get_object_or_404(Filtered_Videos, pk=filtered_objects.id)
    path = filtered_objects.filtered_video.url.split("media")

    with open(settings.MEDIA_ROOT + path[1], "rb") as video_file:
        response = HttpResponse(video_file, content_type="video/mp4")
        response["Content-Disposition"] = f'attachment; filename="{output_file_path}"'
        return response
