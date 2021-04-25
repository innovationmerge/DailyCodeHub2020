# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Linux Encoding conversion Week
# Convert a file from UTF-8 to ASCII//TRANSLIT Encoding using Linux iconv

$ cat input_file.txt
# Output : A E I O U Y

$ file -bi input_file.txt
# Output : text/plain; charset=us-ascii

$ iconv -f us-ascii -t utf-16 input_file.txt -o output_file.txt

$ file -bi input_file.txt
# Output : text/plain; charset=us-ascii

$ cat output_file.txt
# Output : A E I O U Y