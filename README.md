Files to generate sql for entry into mailbox.cws.net

md5crypt.py - Library to generate salted md5 string for passwords

sqlgen.py - Generates sql for a given list of usernames read from the file 'users' reads passwords from a file 'passwords'. Generates sql for insertion into postifx db.

passwords - Example file included. This is pulled from running ngrep

users - list of email addresses seperated by new lines


To sniff out passwords

nohup ngrep "PASS|USER|+OK Mailbox open" -d any port 110 |grep -e USER -e PASS -e 'OK' >>/home/user/passwordlist


spammon.py - Monitors postfix logs for users that may be sending/recieving a lot of spam
   sends email to brian and monitor at cws when a user sends over a set limit in 1 hour
   usage: python spammon.py
   Can be appended to /etc/rc.local with the following
   nohup /path/to/spammon.py &>/var/log/spammon.log &
