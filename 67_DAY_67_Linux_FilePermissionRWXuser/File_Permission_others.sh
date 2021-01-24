# iNNovationMerge

# Remove the read, write, and execute permission 
# for all users except the file’s owner
# Linux from command line using chmod command

# Syntax 
# chmod [OPTIONS] MODE FILE

# Create file with current premissions
$ touch filename.txt

# View current premissions
$ ls -ltr filename.txt
# Output :  
# -rwxrw-rwx 1 ubuntu ubuntu 0 Jan 17 14:50 filename.txt

# provide required permissions
$ chmod og-rwx filename.txt

# View changed premissions
$ ls -ltr filename.txt
# Output :  
# -rwx------ 1 ubuntu ubuntu 0 Jan 17 15:01 filename.txt



