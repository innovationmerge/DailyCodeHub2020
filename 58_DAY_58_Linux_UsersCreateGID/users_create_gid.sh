# iNNovationMerge

# Create new users with Specific Home Directory, Specific User ID & Specific Group ID
# in Linux from command line using useradd command

# Syntax 
# useradd [OPTIONS] USERNAME

# Add a group
$ sudo groupadd group1

# create a new user with username user4 , uuid 1500, group group1 and Home Directory /opt/user4
$ sudo useradd -m -d /opt/user4 -u 1501 -g group1 user4

# Enter password two times
$ sudo passwd user4

# check created directory
$ ls -ltr /opt/user4

# check user ID of user4
$ id -u user4

# check group ID of user4
$ id -gn user4