# iNNovationMerge

# Give read, write and execute permission to the file’s owner,
# read permissions to the file’s group and 
# no permissions to all other users
# Linux from command line using chmod command

# Syntax 
# chmod [OPTIONS] MODE FILE

# Create file with current premissions
$ touch filename.txt

# View current premissions
$ ls -ltr filename.txt
# Output :  
# -rwx------ 1 ubuntu ubuntu 0 Jan 17 15:01 filename.txt

# provide required permissions
$ chmod u=rwx,g=r,o= filename.txt

# View changed premissions
$ ls -ltr filename.txt
# Output :  
# -rwxr----- 1 ubuntu ubuntu 0 Jan 17 15:09 filename.txt



