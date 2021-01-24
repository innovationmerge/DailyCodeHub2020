# iNNovationMerge

# Provide group permission to read, write the file and execute it in Linux from command line using chmod command

# Syntax 
# chmod [OPTIONS] MODE FILE

# Create file with current premissions
$ touch filename.txt

# View current premissions
$ ls -ltr filename.txt
# Output :  
# -rw-r--r-- 1 ubuntu ubuntu 0 Jan 17 12:56 filename.txt

# provide required permissions
$ chmod g=rw filename.txt

# View changed premissions
$ ls -ltr filename.txt
# Output :  
# -rw-rw-r-- 1 ubuntu ubuntu 0 Jan 17 14:32 filename.txt


