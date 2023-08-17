from django.shortcuts import render


def video(request, slug):
    video = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 853846914},
        'instalacao-windows': {'titulo': 'Intalação Windows', 'vimeo_id': 853846914},
    }
    video = video[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
