# iNNovationMerge

# Create new users with Specific Home Directory, Specific User ID & multiple groups
# in Linux from command line using useradd command

# Syntax 
# useradd [OPTIONS] USERNAME

# Add a group
$ sudo groupadd group2

$ sudo groupadd group3

# create a new user with username user5 , uuid 1502, group group1 and Home Directory /opt/user5
$ sudo useradd -m -d /opt/user5 -u 1502 -G group1,group2,group3 user5

# Enter password two times
$ sudo passwd user5

# check created directory
$ ls -ltr /opt/user5

# check user ID of user4
$ id -u user5

# check group ID of user4
$ id user5