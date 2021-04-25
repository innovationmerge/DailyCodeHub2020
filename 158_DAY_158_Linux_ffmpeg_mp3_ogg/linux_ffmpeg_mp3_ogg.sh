# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Linux Encoding conversion Week
# Convert a audio file from mp3 to ogg using Linux ffmpeg

$ file -bi audio.mp3 
# Output : audio/mpeg; charset=binary

$ ffmpeg -i audio.mp3 output.ogg

$ file -bi output.ogg 
# Output : audio/ogg; charset=binary



