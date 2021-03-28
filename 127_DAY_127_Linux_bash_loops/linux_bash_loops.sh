# **************** "iNNovationMerge DailyCodeHub" ****************
# Visit https://www.innovationmerge.com/
# Theme : Week with Bash programming
# Program to explain loops in Bash programming

# Using While Loop:
#!/bin/bash
start=true
count=1
while [ $start ]
do
echo $count
if [ $count -gt 5 ];
then
break
fi
((count++))
done

# Using For Loop:
#!/bin/bash
for (( counter=10; counter>0; counter-- ))
do
echo -n "$counter "
done
printf "\n"

# Using Infinite loops:
#!/bin/bash
for (( ; ; ))
do
   echo "infinite loops [ hit CTRL+C to stop]"
done











