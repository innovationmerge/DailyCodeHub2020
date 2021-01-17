# iNNovationMerge

# Create new users with expiry date in Linux from command line using useradd command

# Syntax 
# useradd [OPTIONS] USERNAME


# create a new user with username user6 and expriy date 2021-01-17
$ sudo useradd -e 2021-01-17 user6

# Enter password two times
$ sudo passwd user6

#  verify the user account expiry date:
$ sudo chage -l user6
