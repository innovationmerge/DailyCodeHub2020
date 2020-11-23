# iNNovationMerge

# Fuzzy parsing of dates from log data

#pip install python-dateutil

from dateutil.parser import parse
logline = 'INFO 2020-11-01T02:14:01 Server Started.'
timestamp = parse(logline, fuzzy=True)
print("Extracted timestamp : " + str(timestamp))

# Extracted timestamp : 2020-11-01 02:14:01

