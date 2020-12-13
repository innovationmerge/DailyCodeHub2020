# iNNovationMerge

# Set timezones in Linux from command line using timedatectl

# Display the current date, time and timezone
timedatectl

<<COMMENT
Output :
      Local time: Thu 2020-11-12 10:25:30 IST
  Universal time: Thu 2020-11-12 04:55:30 UTC
        RTC time: n/a
       Time zone: Asia/Kolkata (IST, +0530)
COMMENT

# List Time zones
timedatectl list-timezones | grep America/N

<<COMMENT
Output :
   America/Nassau
    America/New_York
    America/Nipigon
    America/Nome
    America/Noronha
    America/North_Dakota/Beulah
    America/North_Dakota/Center
    America/North_Dakota/New_Salem
COMMENT

sudo timedatectl set-timezone 'America/New_York'

# Check changed timezone
timedatectl
<<COMMENT
      Local time: Thu 2020-11-12 00:02:26 EST
  Universal time: Thu 2020-11-12 05:02:26 UTC
        RTC time: n/a
       Time zone: America/New_York (EST, -0500)
COMMENT