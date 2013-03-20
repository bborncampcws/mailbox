#!/usr/bin/python
##monitor outgoing emails
##send email if user is sending out too much
import tailer
import re
from datetime import datetime
import smtplib
import socket

tally={}
limit=50
hostname=socket.gethostname()

def start_email():
  #send email about start of monitor program
  toaddr='brian@cws.net'
  fromaddr='alert@mailbox.cws.net'
  msg="From: "+fromaddr+"\r\nTo: "+toaddr+"\r\n\r\n Starting email monitoring on "+hostname
  str(limit)+" emails in the last hour or since you were last notified "
  subject="Mailbox Outgoing Spam Warning"
  server=smtplib.SMTP('localhost')
  server.sendmail(fromaddr, toaddr, msg)
  toaddr='monitor@cws.net'
  server.sendmail(fromaddr, toaddr, msg)
  server.quit()

def alert(email):
  #send email about lots of emails
  toaddr='brian@cws.net'
  fromaddr='alert@mailbox.cws.net'
  msg="From: "+fromaddr+"\r\nTo: "+toaddr+"\r\n\r\nWarning: user "+email+" may be spamming on "+hostname+" They have sent over "+\
  str(limit)+" emails in the last hour or since you were last notified "
  subject="Mailbox Outgoing Spam Warning"
  server=smtplib.SMTP('localhost')
  server.sendmail(fromaddr, toaddr, msg)
  toaddr='monitor@cws.net'
  server.sendmail(fromaddr, toaddr, msg)
  server.quit()


start_email()
alert('TEST ALERT')
for line in tailer.follow(open('/var/log/mail.log')):
  regex=re.compile('qmgr.*from=<(.*)>')
  lineres=regex.search(line)
  if lineres is not None:
    email=lineres.group(1)
    try:
      tally[email]+=1
    except KeyError:
      tally[email]=1
    print email,line
    if tally[email]>limit:
     alert(email)
     tally[email]=0
    if datetime.now().minute==0:
     tally={}


