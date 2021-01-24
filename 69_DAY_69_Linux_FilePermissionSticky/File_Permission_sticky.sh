# iNNovationMerge

# Add a sticky bit to a given file
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
$ chmod o+t filename.txt

# View changed premissions
$ ls -ltr filename.txt
# Output :  
# -rwxr----T 1 ubuntu ubuntu 0 Jan 17 15:18 filename.txt






