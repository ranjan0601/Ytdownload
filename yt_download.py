

import yt_dlp

yt_dlp.YoutubeDL({'format':'best', 'outtmpl': '%(title)s.%(ext)s'}).download(['https://www.youtube.com/watch?v=yRQDzm-GGFQ'])