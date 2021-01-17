# iNNovationMerge

# Create new users with Specific Home Directory
# in Linux from command line using useradd command

# Syntax 
# useradd [OPTIONS] USERNAME

$ sudo useradd -m -d /opt/user2 user2
# create a new user with username user2 and  Home Directory /opt/user2


$ sudo passwd user2
# Enter password two times

# check created directory
$ ls -ltr /opt/user2