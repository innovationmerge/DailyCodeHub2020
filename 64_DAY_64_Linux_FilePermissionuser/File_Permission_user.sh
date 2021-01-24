# iNNovationMerge

# Provide user permission to read, write and execute the file
# Linux from command line using chmod command

# Syntax 
# chmod [OPTIONS] MODE FILE

# Create file with current premissions
$ touch filename.txt

# View current premissions
$ ls -ltr filename.txt
# Output :  
# -rw-rw-r-- 1 ubuntu ubuntu 0 Jan 17 14:43 filename.txt

# provide required permissions
$ chmod u=rwx filename.txt

# View changed premissions
$ ls -ltr filename.txt
# Output :  
# -rwxrw-r-- 1 ubuntu ubuntu 0 Jan 17 14:43 filename.txt


