# iNNovationMerge

# Create new users with password expiry in Linux from command line using useradd command

# Syntax 
# useradd [OPTIONS] USERNAME


# create a new user with username user8
# user expriy date 2021-01-17
$ sudo useradd -e 2021-01-17 user8

# Enter password two times
$ sudo passwd user8

# Check the current user account details
$ sudo chage -l user8

# Change password expiry to 45 Days
$ sudo chage -M 45 user8

# Verify the user account expiry date
$ sudo chage -l user8