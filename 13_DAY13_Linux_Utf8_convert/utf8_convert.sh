# iNNovationMerge

# Easy way to convert Files to UTF-8 Encoding in Linux

# List all known coded character sets
iconv -l

#Convert Files to UTF-8 Encoding
# Syntax - 
# iconv  -f FROM_ENCODING -t UTF-8 INPUT_FILE -o OUTPUT_FILE
iconv -f Windows-1250 -t UTF-8 input.csv -o out.csv