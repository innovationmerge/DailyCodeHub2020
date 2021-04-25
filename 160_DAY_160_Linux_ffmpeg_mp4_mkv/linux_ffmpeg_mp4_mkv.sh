# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Linux Encoding conversion Week
# Convert a video file from mp4 to mkv using Linux ffmpeg

$ file -bi video.mp4 
# Output : video/mp4; charset=binary

$ ffmpeg -i video.mp4 output.mkv

$ file -bi output.mkv
# Output : video/x-matroska; charset=binary



