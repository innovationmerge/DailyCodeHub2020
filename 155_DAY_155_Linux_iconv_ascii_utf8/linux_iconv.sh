# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Linux Encoding conversion Week
# Convert a file from utf-16le to utf-8 Encoding using Linux iconv

$ cat input_file.txt
# Output : ��A E I O U Y

$ file -bi input_file.txt
# Output : text/plain; charset=utf-16le

$ iconv -f utf-16le -t utf-8 input_file.txt -o output_file.txt

$ file -bi output_file.txt
# Output : text/plain; charset=utf-8

$ cat output_file.txt
# Output : A E I O U Y
