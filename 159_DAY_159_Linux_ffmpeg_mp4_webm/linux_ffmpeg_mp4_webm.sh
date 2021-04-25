# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Linux Encoding conversion Week
# Convert a video file from mp4 to webm using Linux ffmpeg

$ file -bi video.mp4 
# Output : video/mp4; charset=binary

$ ffmpeg -i video.mp4 output.webm

$ file -bi output.webm
# Output : video/webm; charset=binary



