
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about/about.html')

def album(request):
    return render(request, 'album/album.html')    

def play(request):
    return render(request, 'play/play.html')     

def download(request):
    return render(request, 'download/download.html')     




# import os
# import tempfile
# from django.http import FileResponse, HttpResponse
# from yt_dlp import YoutubeDL

# def download_mp3(request):
#     url = request.GET.get("url")

#     if not url:
#         return HttpResponse("No URL provided", status=400)

#     # Create temp file WITHOUT extension
#     temp_file = tempfile.NamedTemporaryFile(delete=False)
#     base_path = temp_file.name
#     temp_file.close()

#     # Correct FFmpeg path
#     ffmpeg_dir = r"C:\ffmpeg1\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"

#     ydl_opts = {
#         "format": "251",   # audio only
#         "outtmpl": base_path + ".%(ext)s",
#         "ffmpeg_location": ffmpeg_dir,
#         "postprocessors": [{
#             "key": "FFmpegExtractAudio",
#             "preferredcodec": "mp3",
#             "preferredquality": "192",
#         }],
#         "postprocessor_args": [
#             "-acodec", "libmp3lame"
#         ],
#         "extract_audio": True,
#         "merge_output_format": "mp3",
#         "player_client": "android"
#     }

#     try:
#         with YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])

#         final_mp3 = base_path + ".mp3"
#         return FileResponse(open(final_mp3, "rb"), as_attachment=True, filename="audio.mp3")

#     except Exception as e:
#         return HttpResponse(str(e), status=500)



# import os
# import re
# import tempfile
# from django.http import FileResponse, HttpResponse, JsonResponse
# from yt_dlp import YoutubeDL
# import string

# def sanitize_filename(name):
#     valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
#     return ''.join(c for c in name if c in valid_chars).strip()





# def download_mp3(request):
#     url = request.GET.get("url")
#     format_type = request.GET.get("format", "mp3")   # mp3 / mp4 / wav / m4a
#     quality = request.GET.get("quality", "192")      # 128 / 192 / 320

#     if not url:
#         return HttpResponse("No URL provided", status=400)

#     # Create temporary path
#     temp_dir = tempfile.mkdtemp()
#     output_template = os.path.join(temp_dir, "%(title)s.%(ext)s")

#     # FFmpeg Path
#     ffmpeg_path = r"C:\ffmpeg1\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"

#     # Base yt-dlp options
#     ydl_opts = {
#         "outtmpl": output_template,
#         "ffmpeg_location": ffmpeg_path,
#         "player_client": "android",
#     }

#     # ===============================
#     # AUDIO DOWNLOAD (MP3 / M4A / WAV)
#     # ===============================
#     if format_type in ["mp3", "wav", "m4a"]:

#         # Choose correct codec
#         codec_map = {
#             "mp3": "mp3",
#             "wav": "wav",
#             "m4a": "m4a",
#         }

#         ydl_opts.update({
#             "format": "bestaudio/best",
#             "postprocessors": [{
#                 "key": "FFmpegExtractAudio",
#                 "preferredcodec": codec_map[format_type],
#                 "preferredquality": quality if format_type == "mp3" else "0",
#             }],
#         })

#     # ===============================
#     # VIDEO DOWNLOAD (MP4)
#     # ===============================
#     elif format_type == "mp4":
#         ydl_opts.update({
#             "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
#         })

#     else:
#         return HttpResponse("Invalid format type.", status=400)

#     # ===============================
#     # PROCESS DOWNLOAD
#     # ===============================

#     try:
#         with YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=True)

#         video_title = sanitize_filename(info.get("title", "video"))
#         ext = "mp3" if format_type == "mp3" else format_type

#         # Final output path
#         final_file = os.path.join(temp_dir, f"{video_title}.{ext}")

#         if not os.path.exists(final_file):  # yt-dlp may give dynamic ext
#             # Find any file produced
#             for f in os.listdir(temp_dir):
#                 if f.startswith(video_title):
#                     final_file = os.path.join(temp_dir, f)
#                     break

#         if not os.path.exists(final_file):
#             return HttpResponse("Error generating file.", status=500)

#         # Send file for download
#         return FileResponse(
#             open(final_file, "rb"),
#             as_attachment=True,
#             filename=f"{video_title}.{ext}"
#         )

#     except Exception as e:
#         return HttpResponse(f"Error: {str(e)}", status=500)

################################################################################
# import os
# import string
# import tempfile
# from django.http import FileResponse, HttpResponse
# from yt_dlp import YoutubeDL


# def sanitize_filename(name):
#     valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
#     return ''.join(c for c in name if c in valid_chars).strip()


# def download_mp3(request):
#     url = request.GET.get("url")
#     file_format = request.GET.get("format", "mp3")   # mp3 or mp4
#     quality = request.GET.get("quality", "192")

#     if not url:
#         return HttpResponse("No URL provided", status=400)

#     temp_dir = tempfile.mkdtemp()

#     # Correct ffmpeg path
#     ffmpeg_dir = r"C:\ffmpeg1\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"

#     # ---- STEP 1: Get Video Info ---- #
#     try:
#         info_opts = {"quiet": True, "skip_download": True}
#         with YoutubeDL(info_opts) as ydl:
#             info = ydl.extract_info(url, download=False)

#         title = sanitize_filename(info.get("title", "audio"))
#     except:
#         title = "audio"   # fallback if error

#     output_template = os.path.join(temp_dir, f"{title}.%(ext)s")

#     # ---- STEP 2: Download audio or video ---- #
#     ydl_opts = {
#         "outtmpl": output_template,
#         "ffmpeg_location": ffmpeg_dir,
#         "player_client": "android",
#     }

#     if file_format == "mp3":
#         ydl_opts.update({
#             "format": "bestaudio/best",
#             "postprocessors": [{
#                 "key": "FFmpegExtractAudio",
#                 "preferredcodec": "mp3",
#                 "preferredquality": quality,
#             }],
#         })

#     elif file_format == "mp4":
#         ydl_opts.update({
#             "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
#             "merge_output_format": "mp4",
#         })

#     try:
#         with YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])

#         # ---- STEP 3: Locate final file ---- #
#         for f in os.listdir(temp_dir):
#             if f.startswith(title):
#                 final_file = os.path.join(temp_dir, f)
#                 break

#         return FileResponse(open(final_file, "rb"),
#                             as_attachment=True,
#                             filename=os.path.basename(final_file))

#     except Exception as e:
#         return HttpResponse(str(e), status=500)


# import os
# import string
# import tempfile
# from django.http import FileResponse, HttpResponse
# from yt_dlp import YoutubeDL


# def sanitize_filename(name):
#     valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
#     return ''.join(c for c in name if c in valid_chars).strip()


# def download_mp3(request):
#     url = request.GET.get("url")
#     file_format = request.GET.get("format", "mp3")   # mp3 or mp4

#     if not url:
#         return HttpResponse("No URL provided", status=400)

#     temp_dir = tempfile.mkdtemp()

#     ffmpeg_dir = r"C:\ffmpeg1\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"

#     # ------------------- STEP 1: Get metadata safely -------------------
#     try:
#         info_opts = {"quiet": True, "skip_download": True}
#         with YoutubeDL(info_opts) as ydl:
#             info = ydl.extract_info(url, download=False)

#         title = sanitize_filename(info.get("title", "audio"))
#     except:
#         title = "audio"

#     output_template = os.path.join(temp_dir, f"{title}.%(ext)s")

#     # ------------------- STEP 2: Build yt-dlp options -------------------
#     ydl_opts = {
#         "outtmpl": output_template,
#         "ffmpeg_location": ffmpeg_dir,
#         "player_client": "android",
#         "quiet": True
#     }

#     # ============ A) BEST AUDIO → MP3 320 kbps =============
#     if file_format == "mp3":
#         ydl_opts.update({
#             "format": "bestaudio/best",
#             "postprocessors": [{
#                 "key": "FFmpegExtractAudio",
#                 "preferredcodec": "mp3",
#                 "preferredquality": "0",   # ignored but required
#             }],
#             "postprocessor_args": [
#                 "-acodec", "libmp3lame",
#                 "-b:a", "320k"           # <-- force TRUE 320 kbps
#             ]
#         })

#     # ============ B) BEST VIDEO ≤ 1080p → MP4 =============
#     elif file_format == "mp4":
#         ydl_opts.update({
#             "format": (
#                 "bestvideo[height<=1080][ext=mp4]+"
#                 "bestaudio[ext=m4a]/best[height<=1080]/mp4"
#             ),
#             "merge_output_format": "mp4",
#         })

#     else:
#         return HttpResponse("Invalid format", status=400)

#     # ------------------- STEP 3: Download -------------------
#     try:
#         with YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])

#         # ------------------- STEP 4: Return file -------------------
#         final_file = None
#         for f in os.listdir(temp_dir):
#             if f.startswith(title):
#                 final_file = os.path.join(temp_dir, f)
#                 break

#         if not final_file:
#             return HttpResponse("File not created", status=500)

#         return FileResponse(
#             open(final_file, "rb"),
#             as_attachment=True,
#             filename=os.path.basename(final_file)
#         )

#     except Exception as e:
#         return HttpResponse(str(e), status=500)


import os
import string
import tempfile
from django.http import JsonResponse, FileResponse, HttpResponse
from yt_dlp import YoutubeDL

def sanitize_filename(name):
    valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
    return ''.join(c for c in name if c in valid_chars).strip()


# STEP 1: Fetch info only
def fetch_info(request):
    url = request.GET.get("url")

    if not url:
        return JsonResponse({"error": "Missing URL"}, status=400)

    try:
        ydl_opts = {"quiet": True, "skip_download": True}
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        title = sanitize_filename(info.get("title", "Unknown Title"))
        thumb = info.get("thumbnail")
        duration = info.get("duration")

        return JsonResponse({
            "title": title,
            "thumbnail": thumb,
            "duration": duration,
            "download_url_mp3": f"/download-final/?url={url}&format=mp3",
            "download_url_mp4": f"/download-final/?url={url}&format=mp4"
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# STEP 2: Final download
def download_mp3(request):
    url = request.GET.get("url")
    file_format = request.GET.get("format", "mp3")

    if not url:
        return HttpResponse("Missing URL", status=400)

    ffmpeg_dir = r"C:\ffmpeg1\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin"
    temp_dir = tempfile.mkdtemp()

    info_opts = {"quiet": True, "skip_download": True}
    with YoutubeDL(info_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = sanitize_filename(info.get("title", "media"))

    output_path = os.path.join(temp_dir, f"{title}.%(ext)s")

    ydl_opts = {
        "outtmpl": output_path,
        "ffmpeg_location": ffmpeg_dir,
    }

    if file_format == "mp3":
        ydl_opts.update({
            "format": "bestaudio",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }],
        })
    else:
        ydl_opts.update({
            "format": "bestvideo[height<=1080]+bestaudio/best",
            "merge_output_format": "mp4",
        })

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # find final file
    for f in os.listdir(temp_dir):
        if f.startswith(title):
            final_file = os.path.join(temp_dir, f)
            break

    return FileResponse(open(final_file, "rb"),
                        as_attachment=True,
                        filename=os.path.basename(final_file))





