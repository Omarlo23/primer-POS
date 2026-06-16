import yt_dlp 
import os

def descargar(url, carpeta="Mi musica"):

    try:

        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

        opciones = {
            "format": "bestaudio/best",
            "outtmpl": f"{carpeta}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
        }

        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False