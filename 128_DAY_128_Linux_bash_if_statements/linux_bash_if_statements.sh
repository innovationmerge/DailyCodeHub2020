# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Bash programming
# Program to use if statements in Bash programming

# Using if statement:
#!/bin/bash
check_number=100
if [ $check_number -lt 99 ];
then
echo "It is a two digit number"
else
echo "It is a three digit number"
fi

# Using if statement with logical operations:
#!/bin/bash
echo "Enter your username"
read username
echo "Enter your password"
read password
if [[ ( $username == "innovationmerge" && $password == "dailycodehub365" ) ]]; then
echo "valid iNNovationMerge user"
else
echo "invalid iNNovationMerge user"
fi

# Using else if statement:
#!/bin/bash
echo "Enter number to check"
read check_number
if [ $check_number -lt 10 ];
then
echo "It is a one digit number"
elif [ $check_number -lt 100 ];
then
echo "It is a two digit number"
elif [ $check_number -lt 1000 ];
then
echo "It is a three digit number"
else
echo "It is greater than three digit number"
fi

