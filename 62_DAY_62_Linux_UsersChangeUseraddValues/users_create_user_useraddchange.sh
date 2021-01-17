# iNNovationMerge

# Changing the Default useradd Values in Linux from command line using useradd command

# Syntax 
# useradd [OPTIONS] USERNAME


# view the current default options 
$ sudo useradd -D

# Change the default login shell from /bin/sh to /bin/bash
$ sudo useradd -D -s /bin/bash

# Verify that the default shell value is changed
$ sudo useradd -D | grep -i shell
