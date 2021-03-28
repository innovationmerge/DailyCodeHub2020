# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Bash programming
# Program to understand functions in Bash programming

# Create Function:
#!/bin/bash
function sample_func()
{
echo 'iNNovationMerge'
}

sample_func


# Create function with Parameters:
#!/bin/bash

sum_numbers() {
sum=$(($1 + $2))
echo "Sum is : $sum"
}

sum_numbers 5 6

# Pass Return Value from Function:
#!/bin/bash
function sum_numbers() {
sum=$(($1 + $2))
echo "$sum"
}

sum=$(sum_numbers 5 6)
echo "Return value of 
the sum function is $sum"






