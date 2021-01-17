# iNNovationMerge

# Create new users with Specific Home Directory and Specific User ID
# in Linux from command line using useradd command

# Syntax 
# useradd [OPTIONS] USERNAME

$ sudo useradd -m -d /opt/user3 -u 1500 user3
# create a new user with username user3 , uuid 1500 and  Home Directory /opt/user3


$ sudo passwd user3
# Enter password two times

# check created directory
$ ls -ltr /opt/user3

# check user ID of user4
$ id -u user3
